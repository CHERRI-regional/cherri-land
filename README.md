
### CHERRI-land ###


HOME on ATOS-Bologna is small and it can make sense to install the environments on e.g SCRATCH with modifying poetry.toml:

    [virtualenvs]
      in-project = false
      path = "/scratch/USER/cherri_land_virtualenvs"

    [virtualenvs.options]
       system-site-packages = true

NB! Do not install the whole code on SCRATCH as this is not mounted on the ecflow server

Install with poetry:

    poetry install

Create an experiment and run it:

    poetry run cherri_land -o ai_land.toml --case-name AILand --start-suite


