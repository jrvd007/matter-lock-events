"""Config flow for Matter Lock Events."""

from __future__ import annotations

from homeassistant import config_entries

from .const import DOMAIN, NAME


class MatterLockEventsConfigFlow(
    config_entries.ConfigFlow,
    domain=DOMAIN,
):
    """Handle the Matter Lock Events config flow."""

    VERSION = 1

    async def async_step_user(
        self,
        user_input=None,
    ):
        """Handle the initial step."""

        await self.async_set_unique_id(DOMAIN)
        self._abort_if_unique_id_configured()

        return self.async_create_entry(
            title=NAME,
            data={},
        )