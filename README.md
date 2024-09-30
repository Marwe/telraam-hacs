# Telraam Custom Component for Home Assistant

This custom component integrates Telraam traffic data into Home Assistant, allowing you to monitor car, bike, pedestrian, and night traffic data from your Telraam devices.

## Features

- Monitor traffic data directly in Home Assistant.
- Support for multiple Telraam devices.
- Easy configuration via Home Assistant UI.

## Prerequisites

Before you begin, ensure you have a functioning Home Assistant installation and access to your Telraam API key and device IDs.

## Installation

### Using HACS

This component is compatible with the Home Assistant Community Store (HACS). To install it using HACS, follow these steps:

1. Ensure HACS is installed in your Home Assistant.
2. In HACS, go to "Integrations" and then click the "+ Explore & Download Repositories" button in the bottom right corner.
3. Search for "Telraam" and select this integration.
4. Click "Install this Repository in HACS".
5. Restart Home Assistant.

[![Add to HACS](https://my.home-assistant.io/badges/hacs_default.svg)](hacs:https://github.com/kervel/telraam-hacs)

### Manual Installation

If you prefer not to use HACS, you can install the component manually:

1. Download the `telraam` folder from this repository.
2. Place it into your `config/custom_components/` directory.
3. Restart Home Assistant.

## Configuration

After installation, add the Telraam integration via the Home Assistant UI:

1. Navigate to **Configuration** > **Integrations**.
2. Click on the "+ Add Integration" button.
3. Search for "Telraam" and follow the on-screen instructions to configure the integration with your API key and device ID.

## Support

If you encounter issues or have questions, please file an issue on this GitHub repository.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please feel free to make a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
