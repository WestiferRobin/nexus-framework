from src.models.legions.armada import LegionArmada
from src.utils.fleet_utils import find_fleet_ships_by_type, find_fleet_ship


def find_armada_fleet(armada: LegionArmada, fleet_id):
    if not fleet_id in armada.fleets:
        return None
    armada_fleet = armada.fleets[fleet_id]
    return armada_fleet

def find_armada_ship(armada: LegionArmada, fleet_id, ship_id):
    armada_fleet = find_armada_fleet(armada, fleet_id)
    if armada_fleet is None:
        return None
    legion_ship = find_fleet_ship(armada_fleet, ship_id)
    return legion_ship

def find_armada_ships_by_type(armada: LegionArmada, ship_type: type):
    ships = []
    for fleet in armada.fleets():
        fleet_ships = find_fleet_ships_by_type(fleet, ship_type)
        for ship in fleet_ships:
            ships.append(ship)
    return tuple(ships)
