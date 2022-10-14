# Some NFL Blueprints for Home Assistant

## NFL Game Score Notifications
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fgonzotek%2Fha-nfl%2Fblob%2FBlueprint%2Fblueprints%2Fnfl-game-score-notifications.yaml)

This blueprint will produce mobile app notifications on any score change (td, field goal, extra point), optionally excluding opponent scores. The notification will include data such as the quarter and game clock at the point the score was reported by the api, timeouts remaining, and win probability. It will also report the final score when the game ends. The notifications will be grouped together (separate from other HA notifications) and include metadata tags that allow the individual notifications to be replaced as new scores come in (in practice this works a little bit like Apple’s recently announced Live Activities, where you just see the latest information if you don’t swipe the notification away during a game).

You can track as many games and notify as many devices as you’d like, just select them in the automation.
