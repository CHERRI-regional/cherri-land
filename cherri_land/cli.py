import os
import sys

import tactus
import cherri_land
from tactus.__main__ import main as tactus_main
from tactus.logs import logger
from tactus.os_utils import strip_off_mount_path

def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    
    tmp_mods_output = f"{os.getcwd()}/mods.tmp.{os.getpid()}.toml"
    tactus_path = str(strip_off_mount_path(tactus.__path__[0]))
    cherri_land_path = str(strip_off_mount_path(cherri_land.__path__[0]))
    
    def_config = f"{tactus_path}/data/config_files/config.toml"
    plugin_config = f"{cherri_land_path}/data/config_files/cherri_land.toml"
    with open(tmp_mods_output, mode="w", encoding="utf8") as fhandler:
        fhandler.write("[general.plugin_registry.plugins]\n")
        fhandler.write(f'  cherri_land = "{cherri_land_path}/../"\n')
        fhandler.write('[suite_control]\n')
        fhandler.write('  suite_definition = "AILandSuiteDefinition"\n')
        fhandler.write('[scheduler.ecfvars.troika]\n')
        fhandler.write(f'  config_file = "{cherri_land_path}/data/config_files/troika.yml"\n')
        fhandler.write('[troika]\n')
        fhandler.write(f'  config_file = "{cherri_land_path}/data/config_files/troika.yml"\n')

    argv = ["case", "--config-file", def_config, "--config-data-dir", f"{cherri_land_path}/data/"] + argv
    argv.append(plugin_config)
    argv.append(tmp_mods_output)
    cmd = " ".join(argv)
    logger.info("tactus case command: tactus {}", cmd)
    tactus_main(argv=argv)
    os.remove(tmp_mods_output)

