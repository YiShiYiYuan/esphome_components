from esphome import automation
from esphome.automation import maybe_simple_id
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, uart
from esphome.const import (
    CONF_ID,
    CONF_TEMPERATURE,
    CONF_VOLTAGE,
    CONF_FREQUENCY,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_VOLTAGE,
    DEVICE_CLASS_FREQUENCY,
    STATE_CLASS_MEASUREMENT,
    UNIT_AMPERE,
    UNIT_CELSIUS,
    UNIT_KILOWATT_HOURS,
    UNIT_VOLT,
    UNIT_WATT,
    UNIT_HERTZ,
    STATE_CLASS_TOTAL_INCREASING,
)

from .const import (
    CONF_CURRENT_1,
    CONF_CURRENT_2,
    CONF_CURRENT_3,
    CONF_CURRENT_4,
    CONF_CURRENT_5,
    CONF_CURRENT_6,
    CONF_POWER_1,
    CONF_POWER_2,
    CONF_POWER_3,
    CONF_POWER_4,
    CONF_POWER_5,
    CONF_POWER_6,
    CONF_POWER_SUM,
    CONF_ENERGY_1,
    CONF_ENERGY_2,
    CONF_ENERGY_3,
    CONF_ENERGY_4,
    CONF_ENERGY_5,
    CONF_ENERGY_6,
    CONF_ENERGY_SUM,
)


DEPENDENCIES = ["uart"]
AUTO_LOAD = ["bl0906"]

bl0906_ns = cg.esphome_ns.namespace("bl0906")
BL0906 = bl0906_ns.class_("BL0906", cg.PollingComponent, uart.UARTDevice)

ResetEnergyAction = bl0906_ns.class_("ResetEnergyAction", automation.Action)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(BL0906),
            cv.Optional(CONF_FREQUENCY): sensor.sensor_schema(
                unit_of_measurement=UNIT_HERTZ,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_FREQUENCY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_VOLTAGE): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_VOLTAGE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_CURRENT_1): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE,
                accuracy_decimals=3,
                device_class=DEVICE_CLASS_CURRENT,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_CURRENT_2): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE,
                accuracy_decimals=3,
                device_class=DEVICE_CLASS_CURRENT,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_CURRENT_3): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE,
                accuracy_decimals=3,
                device_class=DEVICE_CLASS_CURRENT,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_CURRENT_4): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE,
                accuracy_decimals=3,
                device_class=DEVICE_CLASS_CURRENT,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_CURRENT_5): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE,
                accuracy_decimals=3,
                device_class=DEVICE_CLASS_CURRENT,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_CURRENT_6): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE,
                accuracy_decimals=3,
                device_class=DEVICE_CLASS_CURRENT,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_POWER_1): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_POWER_2): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_POWER_3): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_POWER_4): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_POWER_5): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_POWER_6): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_POWER_SUM): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_ENERGY_1): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=3,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
            ),
            cv.Optional(CONF_ENERGY_2): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=3,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
            ),
            cv.Optional(CONF_ENERGY_3): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=3,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
            ),
            cv.Optional(CONF_ENERGY_4): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=3,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
            ),
            cv.Optional(CONF_ENERGY_5): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=3,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
            ),
            cv.Optional(CONF_ENERGY_6): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=3,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
            ),
            cv.Optional(CONF_ENERGY_SUM): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=3,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
            ),
        }
    )
    .extend(cv.polling_component_schema("60s"))
    .extend(uart.UART_DEVICE_SCHEMA)
)


@automation.register_action(
    "bl0906.reset_energy",
    ResetEnergyAction,
    maybe_simple_id(
        {
            cv.Required(CONF_ID): cv.use_id(BL0906),
        }
    ),
)
async def reset_energy_to_code(config, action_id, template_arg, args):
    paren = await cg.get_variable(config[CONF_ID])
    return cg.new_Pvariable(action_id, template_arg, paren)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    # if frequency_config := config.get(CONF_FREQUENCY):
    #     sens = await sensor.new_sensor(frequency_config)
    #     cg.add(var.set_frequency_sensor(sens))
    # if temperature_config := config.get(CONF_TEMPERATURE):
    #     sens = await sensor.new_sensor(temperature_config)
    #     cg.add(var.set_temperature_sensor(sens))
    # if voltage_config := config.get(CONF_VOLTAGE):
    #     sens = await sensor.new_sensor(voltage_config)
    #     cg.add(var.set_voltage_sensor(sens))
    # if current_1_config := config.get(CONF_CURRENT_1):
    #     sens = await sensor.new_sensor(current_1_config)
    #     cg.add(var.set_current_sensor_1(sens))
    # if current_2_config := config.get(CONF_CURRENT_2):
    #     sens = await sensor.new_sensor(current_2_config)
    #     cg.add(var.set_current_sensor_2(sens))
    # if current_3_config := config.get(CONF_CURRENT_3):
    #     sens = await sensor.new_sensor(current_3_config)
    #     cg.add(var.set_current_sensor_3(sens))
    # if current_4_config := config.get(CONF_CURRENT_4):
    #     sens = await sensor.new_sensor(current_4_config)
    #     cg.add(var.set_current_sensor_4(sens))
    # if current_5_config := config.get(CONF_CURRENT_5):
    #     sens = await sensor.new_sensor(current_5_config)
    #     cg.add(var.set_current_sensor_5(sens))
    # if current_6_config := config.get(CONF_CURRENT_6):
    #     sens = await sensor.new_sensor(current_6_config)
    #     cg.add(var.set_current_sensor_6(sens))
    # if power_1_config := config.get(CONF_POWER_1):
    #     sens = await sensor.new_sensor(power_1_config)
    #     cg.add(var.set_power_sensor_1(sens))
    # if power_2_config := config.get(CONF_POWER_2):
    #     sens = await sensor.new_sensor(power_2_config)
    #     cg.add(var.set_power_sensor_2(sens))
    # if power_3_config := config.get(CONF_POWER_3):
    #     sens = await sensor.new_sensor(power_3_config)
    #     cg.add(var.set_power_sensor_3(sens))
    # if power_4_config := config.get(CONF_POWER_4):
    #     sens = await sensor.new_sensor(power_4_config)
    #     cg.add(var.set_power_sensor_4(sens))
    # if power_5_config := config.get(CONF_POWER_5):
    #     sens = await sensor.new_sensor(power_5_config)
    #     cg.add(var.set_power_sensor_5(sens))
    # if power_6_config := config.get(CONF_POWER_6):
    #     sens = await sensor.new_sensor(power_6_config)
    #     cg.add(var.set_power_sensor_6(sens))
    # if power_sum_config := config.get(CONF_POWER_SUM):
    #     sens = await sensor.new_sensor(power_sum_config)
    #     cg.add(var.set_power_sensor_sum(sens))
    # if energy_1_config := config.get(CONF_ENERGY_1):
    #     sens = await sensor.new_sensor(energy_1_config)
    #     cg.add(var.set_energy_sensor_1(sens))
    # if energy_2_config := config.get(CONF_ENERGY_2):
    #     sens = await sensor.new_sensor(energy_2_config)
    #     cg.add(var.set_energy_sensor_2(sens))
    # if energy_3_config := config.get(CONF_ENERGY_3):
    #     sens = await sensor.new_sensor(energy_3_config)
    #     cg.add(var.set_energy_sensor_3(sens))
    # if energy_4_config := config.get(CONF_ENERGY_4):
    #     sens = await sensor.new_sensor(energy_4_config)
    #     cg.add(var.set_energy_sensor_4(sens))
    # if energy_5_config := config.get(CONF_ENERGY_5):
    #     sens = await sensor.new_sensor(energy_5_config)
    #     cg.add(var.set_energy_sensor_5(sens))
    # if energy_6_config := config.get(CONF_ENERGY_6):
    #     sens = await sensor.new_sensor(energy_6_config)
    #     cg.add(var.set_energy_sensor_6(sens))
    # if energy_sum_config := config.get(CONF_ENERGY_SUM):
    #     sens = await sensor.new_sensor(energy_sum_config)
    #     cg.add(var.set_energy_sensor_sum(sens))

    for element, set_func in [
        (CONF_FREQUENCY, var.set_frequency_sensor),
        (CONF_TEMPERATURE, var.set_temperature_sensor),
        (CONF_VOLTAGE, var.set_voltage_sensor),
        (CONF_CURRENT_1, var.set_current_sensor_1),
        (CONF_CURRENT_2, var.set_current_sensor_2),
        (CONF_CURRENT_3, var.set_current_sensor_3),
        (CONF_CURRENT_4, var.set_current_sensor_4),
        (CONF_CURRENT_5, var.set_current_sensor_5),
        (CONF_CURRENT_6, var.set_current_sensor_6),
        (CONF_POWER_1, var.set_power_sensor_1),
        (CONF_POWER_2, var.set_power_sensor_2),
        (CONF_POWER_3, var.set_power_sensor_3),
        (CONF_POWER_4, var.set_power_sensor_4),
        (CONF_POWER_5, var.set_power_sensor_5),
        (CONF_POWER_6, var.set_power_sensor_6),
        (CONF_POWER_SUM, var.set_power_sensor_sum),
        (CONF_ENERGY_1, var.set_energy_sensor_1),
        (CONF_ENERGY_2, var.set_energy_sensor_2),
        (CONF_ENERGY_3, var.set_energy_sensor_3),
        (CONF_ENERGY_4, var.set_energy_sensor_4),
        (CONF_ENERGY_5, var.set_energy_sensor_5),
        (CONF_ENERGY_6, var.set_energy_sensor_6),
        (CONF_ENERGY_SUM, var.set_energy_sensor_sum),
    ]:
        if element_config := config.get(element):
            sens = await sensor.new_sensor(element_config)
            cg.add(set_func(sens))
