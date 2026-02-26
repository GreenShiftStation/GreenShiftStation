import codecs
import hashlib
import io
import zipfile
import subprocess
import os
import datetime
import shutil
import json

CLIENT_FILE_NAME="SS14.Client.zip"
LINUX_X64_FILE_NAME="SS14.Server_linux-x64.zip"
LINUX_ARM64_FILE_NAME="SS14.Server_linux-arm64.zip"
OSX_X64_FILE_NAME="SS14.Server_osx-x64.zip"
WIN_X64_FILE_NAME="SS14.Server_win-x64.zip"
OSX_ARM64_FILE_NAME="SS14.Server_osx-arm64.zip"
WIN_ARM64_FILE_NAME="SS14.Server_win-arm64.zip"

FILES = [
    CLIENT_FILE_NAME,
    LINUX_ARM64_FILE_NAME,
    LINUX_X64_FILE_NAME,
    WIN_ARM64_FILE_NAME,
    WIN_X64_FILE_NAME,
    OSX_ARM64_FILE_NAME,
    OSX_X64_FILE_NAME
]

def generate_manifest_hash(file: str) -> str:
    """
    will be used when/if we update to the new wizden manifest setup?
    idfk. The docs are actually shit.
    """
    zip = zipfile.ZipFile(file)
    infos = zip.infolist()
    infos.sort(key=lambda i: i.filename)

    bytesIO = io.BytesIO()
    writer = codecs.getwriter("UTF-8")(bytesIO)
    writer.write("Robust Content Manifest 1\n")

    for info in infos:
        if info.filename[-1] == "/":
            continue

        bytes = zip.read(info)
        hash = hashlib.blake2b(bytes, digest_size=32).hexdigest().upper()
        writer.write(f"{hash} {info.filename}\n")

    manifestHash = hashlib.blake2b(bytesIO.getbuffer(), digest_size=32)

    return manifestHash.hexdigest().upper()

def sha_256(text: str):
    return hashlib.sha256(text.encode()).hexdigest()

def sha_256_file(file_path: str):
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda:f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest().upper()

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.abspath(os.path.join(script_dir, "../.."))

    # Assert we are on a clean commit
    git_status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=project_dir)
    try:
        assert git_status.stdout.strip() == ""
    except AssertionError as e:
        print(f"Uncommitted changes:\n{git_status.stdout}\n\nCannot build manifest. Exiting")
        exit()

    commit_hash = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        cwd=project_dir
    ).stdout.strip()

    release_hash = commit_hash[:24] # first 24 characters of the current git hash
    release_dir = os.path.join(project_dir, "release")
    release_final_dir = os.path.join(release_dir, release_hash)
    if os.path.exists(release_final_dir):
        shutil.rmtree(release_final_dir)
    os.makedirs(release_final_dir, exist_ok=False)

    # Build the packager project
    build_packager_process = subprocess.Popen(
        ["dotnet",
         "build",
         "Content.Packaging",
         "--configuration",
         "Release",
         "--no-restore",
         "/m"],
        stdout=subprocess.PIPE,
        text=True,
        cwd=project_dir
    )

    for line in build_packager_process.stdout:
        print(line, end="")
    print("\n\nBuild complete, packaging project")

    # Package our build
    package_server_process = subprocess.Popen(
        ["dotnet", 
         "run", 
         "--project", 
         "Content.Packaging", 
         "server",
         "--hybrid-acz",
         "--platform",
         "linux-arm64",
         "--platform",
         "linux-x64",
         "--platform",
         "win-x64",
         "--platform",
         "osx-x64",
         "--platform",
         "win-arm64",
         "--platform",
         "osx-arm64",
         "--no-wipe-release"], # Currently I am just building this locally, so I want to keep the different releases for backup reasons.
        stdout=subprocess.PIPE,
        text=True,
        cwd=project_dir
    )

    for line in package_server_process.stdout:
        print(line, end="")

    print(f"\n\nPackaging complete")

    print("="*80)
    print("Constructing manifest")
    
    tz = datetime.datetime.now().isoformat()

    new_client_file = os.path.join(release_final_dir, CLIENT_FILE_NAME)
    new_linux_64_file = os.path.join(release_final_dir, LINUX_X64_FILE_NAME)
    new_linux_arm_file = os.path.join(release_final_dir, LINUX_ARM64_FILE_NAME)
    new_osx_64_file = os.path.join(release_final_dir, OSX_X64_FILE_NAME)
    new_osx_arm_file = os.path.join(release_final_dir, OSX_ARM64_FILE_NAME)
    new_win_64_file = os.path.join(release_final_dir, WIN_X64_FILE_NAME)
    new_win_arm_file = os.path.join(release_final_dir, WIN_ARM64_FILE_NAME)

    shutil.move(os.path.join(release_dir, CLIENT_FILE_NAME), new_client_file)
    shutil.move(os.path.join(release_dir, LINUX_X64_FILE_NAME), new_linux_64_file)
    shutil.move(os.path.join(release_dir, LINUX_ARM64_FILE_NAME), new_linux_arm_file)
    shutil.move(os.path.join(release_dir, OSX_X64_FILE_NAME), new_osx_64_file)
    shutil.move(os.path.join(release_dir, OSX_ARM64_FILE_NAME), new_osx_arm_file)
    shutil.move(os.path.join(release_dir, WIN_X64_FILE_NAME), new_win_64_file)
    shutil.move(os.path.join(release_dir, WIN_ARM64_FILE_NAME), new_win_arm_file)

    meta_json = {
        "time": tz,
        "client": {
            "file": CLIENT_FILE_NAME,
            "sha256": sha_256_file(new_client_file)
        },
        "server": {
            "linux-x64": {
                "file": LINUX_X64_FILE_NAME,
                "sha256": sha_256_file(new_linux_64_file)
            },
            "linux-arm64": {
                "file": LINUX_ARM64_FILE_NAME,
                "sha256": sha_256_file(new_linux_arm_file)
            },
            "osx-x64": {
                "file": OSX_X64_FILE_NAME,
                "sha256": sha_256_file(new_osx_64_file)
            },
            "osx-arm64": {
                "file": OSX_ARM64_FILE_NAME,
                "sha256": sha_256_file(new_osx_arm_file)
            },
            "win-x64": {
                "file": WIN_X64_FILE_NAME,
                "sha256": sha_256_file(new_win_64_file)
            },
            "win-arm64": {
                "file": WIN_ARM64_FILE_NAME,
                "sha256": sha_256_file(new_win_arm_file)
            }
        }
    }

    with open(os.path.join(release_final_dir, "meta.json"), "w") as f:
        json.dump(meta_json, f, indent=2)
