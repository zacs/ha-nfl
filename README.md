# NFL game data in Home Assistant

This integration fetches data from current NFL games and presents the data as a variety of sensors. 

The integration is a shameless fork of the excellent [NWS alerts](https://github.com/finity69x2/nws_alerts) custom component by @finity69x2. 

## Installation:

<b>Manually:</b>

Clone or download this repository and copy the "nfl" directory to your "custom_components" directory in your config directory

```<config directory>/custom_components/nfl/...```
  
<b>HACS:</b>

open the HACS section of Home Assistant.

Click the "+ Explore & Add New repositories" button in the bottom right corner.

In the window that opens search for "NFL".

In the window that opens when you select it click om "Install This Repository in HACS"

After installing the integration you can then configure it using the instructions in the following section.
  
## Configuration:

Your team ID will be a 2- or 3-letter acronym (eg. "SEA" for Seattle or "NE" for New England). You can find yours at https://espn.com/nfl in the top scores bar. 

<b>Manually via an entry in your configuration.yaml file:</b>

To create a sensor instance add the following configuration to your sensor definitions using the team_id found above:

```
- platform: nfl
  team_id: 'SEA'
```

After you restart Home Assistant then you should have a new sensor called "sensor.nfl" in your system.

You can overide the sensor default name ("sensor.nfl_score") to one of your choosing by setting the "name:" option:

```
- platform: nfl
  team_id: 'SEA'
  name: Seattle Game Sensor
```

Using the configuration example above the sensor will then be called "sensor.my_nfl_sensor"

<b>Or you can configure the integration via the "Configuration->Integrations" section of the Home Assistant UI.</b>

Look for the integration labeled "NFL"

