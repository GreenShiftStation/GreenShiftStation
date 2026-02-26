# This is a TODO of approved priority changes that anyone can work on.
## This shortlist is here as a tool for our early development, so anyone with the repo can easily look and find something to do without referencing the docs.
If you are working on one of these, but have not completed it, add @<your_username> next to the task

## Immediate Priority
- [x] Get the server running with watchdog etc.
- [x] Get a release workflow in place
- [x] Set up docs repo
- [x] Set up github repo relays to discord

## High Priority
- [ ] Antag System / round removal prevention system
    - [ ] Only command and security spawn on station at round start and respawn
    - [ ] everyone else spawns at arrivals, which should be a custom sub map for each station
        - [ ] arrivals shuttle leaves this station after 5 minutes, and every 5 minutes after
    - [ ] Command and security has 8 minutes alone on station at round start (3 minute flight from arrivals)
    - [ ] Arrivals area on every station should be secure and have a checkpoint for security to vet new crew
- [ ] Make "Intern" role - change assistant
- [ ] MAPS
    - You can modify an existing map to meet some additional requirements, or make a map from scratch.
        *REQUIREMENTS*
        - The station arrivals area must have a security checkpoint, and must be ready to easily add turnstiles requiring "crew" access, and aside from these turnstiles, should not be exitable without hacking a door unless you have accesses.
        - midpop and lowpop maps should not have traditional command roles.
        *OPTIONAL BUT DESIRED, and eventually required*
        - Custom planetside arrivals station to go with your map
        - Custom arrivals shuttle
        - Custom Cargo shuttle
        - Custom evac shuttle
    *ADDITIONAL INFO*
    On GreenShift maps are not all going to have every role, and I intend for map differences to be a reasonably strong factor in roundflow.
    For example, one station may be orbiting a gas giant and contain a special engineering machine, the gas extractor, and roundflow will revolve around engineering maintaining and upgrading this machine with the support of other departments. Another station may be science focused, and most departments are acting as support to the science department.

    I want at least one original map for each pop size, and *ideally*, our maps will be something that set us apart and make the community unique. But if thats not something we can accomplish before we open to the public, I do want a small map pool of adapted maps (only 3 maps) so that we can laser focus on feedback and concept development. Maps as a driving factor of role play is a very slept on concept.
    - [ ] Lowpop station @JoulesBerg
        - Max 10 pop
    - [ ] Midpop Station
        - Min 8 pop
        - Max 40 pop
    - [ ] Highpop Station
        - CAN HAVE TRADITIONAL COMMAND ROLES
        - Min 25 pop
        - Max 100 pop


## Medium Priority
- [] Fix turnstiles to properly support accesses and not allow dragthrough
- [] Add recruitment console that gives base "crew" access type only - for security checkpoint at stationside arrivals. This can be hardcoded to require "Security" access to use, but a full implementation of access configuration to use the device would be cool.
- [] Make it so all players spawn at arrivals unless they are command or security.
    - [] remove or migrate all stationside spawn points that are not for these roles.
- [] Make a tracker of what characters have already been played in a round, and make it so anyone can late join as a character that has not yet been played, but only as a "new hire" role

## Low Priority
- [] If a mindshield implant is injected into an antag, their head explodes
