from models.prisms.model import PrismDrone
from models.fotf.engines.nexus_engine import NexusEngine
from models.fotf.weapons.range_weapons.vehicle_weapons.cannon_weapon import LaserCannon


class SpaceSpeeder:
    def __init__(self, pilot: PrismDrone, right_cannon: LaserCannon = None, left_cannon: LaserCannon = None):
        super().__init__(
            pilot=pilot,
            engines=(
                NexusEngine(pilot.id),
                NexusEngine(pilot.id),
                NexusEngine(pilot.id),
                NexusEngine(pilot.id)
            )
        )
        self.hull = 100
        self.right_cannon = LaserCannon() if right_cannon is None else right_cannon
        self.left_cannon = LaserCannon() if left_cannon is None else left_cannon

