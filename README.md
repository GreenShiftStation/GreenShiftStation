# Shitty README for GreenShift (placeholder)

Greenshift is a fork of Space Station 14, where nothing ever happens.

## Getting Started
There are three default builds that serve different purposes. 
- Debug: For debugging and making code changes, has extra checks and assertions for coding safety
- Tools: For testing and mapping, and stuff
- Release: Self explainatory probably.

Theres more to it than that, but for getting started thats really all thats important. 
Depending on what you are trying to do, use the appropriate build script.

### Step 1
in your command line, or git bash, or whatever the hell you use, run git submodule update --init --recursive
    - This makes sure that your version of robust toolbox is correct, and also that its actually pulled from git correctly. Recursive means that it also pulls in all its own requirements. 

### Step 2
run the appropriate build script. The scripts are all set up by default to AVOID caching build information, this does mean that rebuilding can take longer, but it avoids build cache errors and is generally a best practice. If its too slow, feel free to LOCALLY modify the script by removing the --no-incremental arguments. But when the pipeline runs, that argument will be present, so at the very least, test your final changes with that argument before creating a PR.

### Step 3
Run the runserver and the runclient scripts to get started messing with a local server.

## Contributing
### Expectations
You are expected to THOROUGHLY test your changes before submitting a PR. Its expected that some things will sometimes be missed and bugs will occur, but if you show a pattern of submitting untested, extremely buggy, or non functional content you will be barred from further contributions to the repository on an appeal only basis. We do not have a quality assurance team, and introducing untested, untriaged, game breaking changes to the live servers is not a practice we intend to participate in.
<more stuff here>

### Guidelines
There is a convenient method of system extension in c#. When possible, if changes to an existing upststream system are necessary, it is preferred to create a system extension with its own functions and call those function in the parent, rather than drastically modify the existing update function. This prevents upstream merge conflicts, as there is little to no room for modifications to the same lines of code between the two repositories. If you must make changes to the functions of an existing system, surround your changes in `//greenshift - <reason>` comments so its obvious why a change exists and a decision can be made at the time of the upstream merge whether or not to keep the change, refactor it, or remove it. PR's that make changes to existing systems without such comments will be denied.
<more stuff here>

## License

All code for the content repository is licensed under the [MIT license](https://github.com/GreenShiftStation/GreenShiftStation/blob/master/LICENSE.TXT).  

Most assets are licensed under [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) unless stated otherwise. Assets have their license and copyright specified in the metadata file. For example, see the [metadata for a crowbar](https://github.com/GreenShiftStation/GreenShiftStation/blob/master/Resources/Textures/Objects/Tools/crowbar.rsi/meta.json).  

> [!NOTE]
> Some assets are licensed under the non-commercial [CC-BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/) or similar non-commercial licenses and will need to be removed if you wish to use this project commercially.
