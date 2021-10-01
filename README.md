# NFL game data in Home Assistant

This integration fetches data for a specific NFL team's current/future game, and presents the data as a sensor with attributes for most details of the game. 

The integration is a shameless fork of the excellent [NWS alerts](https://github.com/finity69x2/nws_alerts) custom component by @finity69x2.Thank you for the starting place!

## Installation:

### Manually

Clone or download this repository and copy the "nfl" directory to your "custom_components" directory in your config directory

```<config directory>/custom_components/nfl/...```
  
### HACS

Open the HACS section of Home Assistant.

Click the "..." button in the top right corner and select "Customer Repositories."

In the window that opens paste this Github URL.

In the window that opens when you select it click om "Install This Repository in HACS"

After installing the integration you can then configure it using the instructions in the following section.
  
## Configuration:

You'll need to know your team ID, which is a 2- or 3-letter acronym (eg. "SEA" for Seattle or "NE" for New England). You can find yours at https://espn.com/nfl in the top scores UI. 

### Via the "Configuration->Integrations" section of the Home Assistant UI

Look for the integration labeled "NFL" and enter your team's acronym in the UI prompt. There are also fields for refresh interval and timeout, which are safe to keep as-is. 

### Manually in your configuration.yaml file

To create a sensor instance add the following configuration to your sensor definitions using the team_id found above:

```
- platform: nfl
  team_id: 'SEA'
```

After you restart Home Assistant then you should have a new sensor called `sensor.nfl` in your system.

You can overide the sensor default name ("sensor.nfl_score") to one of your choosing by setting the "name:" option:

```
- platform: nfl
  team_id: 'SEA'
  name: Seattle Game Sensor
```

Using the configuration example above the sensor will then be called "sensor.my_nfl_sensor"
