"""Offline suite."""
from pathlib import Path

from tactus.datetime_utils import as_datetime, as_timedelta, get_decadal_list, get_decade
from tactus.logs import logger
from tactus.suites.base import (
    EcflowSuiteFamily,
    EcflowSuiteTask,
    EcflowSuiteTrigger,
    EcflowSuiteTriggers,
    SuiteDefinition,
)



class AILandSuiteDefinition(SuiteDefinition):
    """Surfex suite."""

    def __init__(
        self,
        config,
        dry_run=False,
    ):
        """Initialize a SurfexSuite object.

        Args:
        ----
            suite_name (str): Name of the suite
            config (ParsedConfig): Parsed configuration
            dry_run (str, optional): Dry run. Defaults to False

        Raises:
        ------
            NotImplementedError: Not implmented

        """
        SuiteDefinition.__init__(self, config, dry_run=dry_run)

        template = Path(__file__).parent.resolve() / "../templates/ecflow/default.py"
        template = template.as_posix()

        inference = EcflowSuiteFamily("inference", self.suite, self.ecf_files)
        EcflowSuiteTask(
            "AILand",
            inference,
            config,
            self.task_settings,
            self.ecf_files,
            input_template=template,
        )
