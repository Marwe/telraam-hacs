from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.entity import DeviceInfo

from .const import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities: AddEntitiesCallback):
    """Set up Telraam sensors from a config entry."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([
        TelraamSensor(coordinator, "car"),
        TelraamSensor(coordinator, "bike"),
        TelraamSensor(coordinator, "pedestrian"),
        TelraamSensor(coordinator, "night")
    ], True)

class TelraamSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, traffic_type):
        super().__init__(coordinator)
        self.coordinator = coordinator
        self._traffic_type = traffic_type
        self._attributes = {}
        self._attr_unique_id = f"{coordinator.device_id}_{traffic_type}"  # Unique ID
        if traffic_type == 'night':
           self._attr_name = f"Night mode on"
        else:
           self._attr_name = f"Telraam {traffic_type.capitalize()} Count"


    @property
    def state(self):
        svalue = self.coordinator.data.get(self._traffic_type)
        if svalue is not None:
           return float(svalue)
        return svalue

    @property
    def device_info(self):
        """Return information about the device."""
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.device_id)},
            name=f"Telraam Traffic Counter ({self.coordinator.device_id})",
            manufacturer="Telraam",
            model="API v1",
            configuration_url="https://telraam.net"
        )

    @property
    def extra_state_attributes(self):
        return self._attributes
