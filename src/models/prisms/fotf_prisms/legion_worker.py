from src.configs.prism_config import PrismConfig
from src.models.prisms.model import PrismDrone


class LegionWorker(PrismDrone):
    def __init__(self, config: PrismConfig):
        super().__init__(config)
