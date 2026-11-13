"""Run AI land script."""
import os


from tactus.logs import logger
from tactus.tasks.base import Task
from tactus.tasks.batch import BatchJob


class AILand(Task):
    """Make offline binaries.

    Args:
        Task (_type_): _description_

    """

    def __init__(self, config) -> None:
        """Construct task.

        Args:
            config (deode.ParsedConfig): Configuration
        """
        Task.__init__(self, config, __class__.__name__)

    def execute(self):
        """Execute."""
        rte = {**os.environ}
        wrapper = ""

        cmd = "ai_land.sh"
        BatchJob(rte, wrapper=wrapper).run(cmd)
