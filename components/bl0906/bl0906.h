#pragma once

#include "esphome/core/automation.h"
#include "esphome/core/component.h"
#include "esphome/core/datatypes.h"
#include "esphome/components/uart/uart.h"
#include "esphome/components/sensor/sensor.h"

namespace esphome {
namespace bl0906 {

// 硬件资料
// https://www.belling.com.cn/media/file_object/bel_product/BL0906/guide/BL0906%20APP%20Note_V1.02.pdf
// https://www.belling.com.cn/media/file_object/bel_product/BL0906/datasheet/BL0906_V1.02_cn.pdf

static const float BL0906_WATT = 16 * 1.097 * 1.097 * (20000 + 20000 + 20000 + 20000 + 20000) /
                                 (40.41259 * ((5.1 + 5.1) * 1000 / 2000) * 1 * 100 * 1 * 1000);  // 总功率转换*16

static const float BL0906_CF = 16 * 4194304 * 0.032768 * 16 /
                               (3600000 * 16 *
                                (40.4125 * ((5.1 + 5.1) * 1000 / 2000) * 1 * 100 * 1 * 1000 /
                                 (1.097 * 1.097 * (20000 + 20000 + 20000 + 20000 + 20000))));  // 总电量转换*16

static const float BL0906_FREF = 10000000;        // 频率转换
static const float BL0906_TREF = 12.5 / 59 - 40;  // 温度转换 内部温度=（TPS-64）*12.5/59-40 （℃）
static const float BL0906_IREF = 1.097 / (12875 * 1 * (5.1 + 5.1) * 1000 / 2000);  // 电流值转换
static const float BL0906_UREF =
    1.097 * (20000 + 20000 + 20000 + 20000 + 20000) / (13162 * 1 * 100 * 1000);  // 电压值转换
static const float BL0906_PREF = 1.097 * 1.097 * (20000 + 20000 + 20000 + 20000 + 20000) /
                                 (40.41259 * ((5.1 + 5.1) * 1000 / 2000) * 1 * 100 * 1 * 1000);  // 功率值转换
static const float BL0906_EREF = 4194304 * 0.032768 * 16 /
                                 (3600000 * 16 *
                                  (40.4125 * ((5.1 + 5.1) * 1000 / 2000) * 1 * 100 * 1 * 1000 /
                                   (1.097 * 1.097 * (20000 + 20000 + 20000 + 20000 + 20000))));  // 电量值转换
static const float BL0906_ki = 12875 * 1 * (5.1 + 5.1) * 1000 / 2000 / 1.097;                    // 电流系数
static const float BL0906_Kp = 40.4125 * ((5.1 + 5.1) * 1000 / 2000) * 1 * 100 * 1 * 1000 / 1.097 / 1.097 /
                               (20000 + 20000 + 20000 + 20000 + 20000);  // 功率系数
// 注意：字节顺序为大端模式(big
// endian)：数据的高位字节保存在内存的低地址中，而低位字节保存在内存的高地址中。（低-中-高）

struct DataPacket {  // NOLINT(altera-struct-pack-align)
  uint8_t l;
  uint8_t m;
  uint8_t h;
  uint8_t checksum;  // checksum
  uint8_t address;
} __attribute__((packed));

struct ube24_t {  // NOLINT(readability-identifier-naming,altera-struct-pack-align)
  uint8_t l;
  uint8_t m;
  uint8_t h;
} __attribute__((packed));

struct sbe24_t {  // NOLINT(readability-identifier-naming,altera-struct-pack-align)
  uint8_t l;
  uint8_t m;
  int8_t h;
} __attribute__((packed));

typedef enum process_state_ { PROCESS_DONE = 0 } process_state;

template<typename... Ts> class ResetEnergyAction;
class BL0906;
typedef void (BL0906::*ActionCallbackFuncPtr)(void);

class BL0906 : public PollingComponent, public uart::UARTDevice {
 public:
  void set_voltage_sensor(sensor::Sensor *voltage_sensor) { voltage_sensor_ = voltage_sensor; }
  void set_current_sensor_1(sensor::Sensor *current_sensor_1) { current_sensor_1_ = current_sensor_1; }
  void set_current_sensor_2(sensor::Sensor *current_sensor_2) { current_sensor_2_ = current_sensor_2; }
  void set_current_sensor_3(sensor::Sensor *current_sensor_3) { current_sensor_3_ = current_sensor_3; }
  void set_current_sensor_4(sensor::Sensor *current_sensor_4) { current_sensor_4_ = current_sensor_4; }
  void set_current_sensor_5(sensor::Sensor *current_sensor_5) { current_sensor_5_ = current_sensor_5; }
  void set_current_sensor_6(sensor::Sensor *current_sensor_6) { current_sensor_6_ = current_sensor_6; }
  void set_power_sensor_1(sensor::Sensor *power_sensor_1) { power_sensor_1_ = power_sensor_1; }
  void set_power_sensor_2(sensor::Sensor *power_sensor_2) { power_sensor_2_ = power_sensor_2; }
  void set_power_sensor_3(sensor::Sensor *power_sensor_3) { power_sensor_3_ = power_sensor_3; }
  void set_power_sensor_4(sensor::Sensor *power_sensor_4) { power_sensor_4_ = power_sensor_4; }
  void set_power_sensor_5(sensor::Sensor *power_sensor_5) { power_sensor_5_ = power_sensor_5; }
  void set_power_sensor_6(sensor::Sensor *power_sensor_6) { power_sensor_6_ = power_sensor_6; }
  void set_power_sensor_sum(sensor::Sensor *power_sensor_sum) { power_sensor_sum_ = power_sensor_sum; }
  void set_energy_sensor_1(sensor::Sensor *energy_sensor_1) { energy_sensor_1_ = energy_sensor_1; }
  void set_energy_sensor_2(sensor::Sensor *energy_sensor_2) { energy_sensor_2_ = energy_sensor_2; }
  void set_energy_sensor_3(sensor::Sensor *energy_sensor_3) { energy_sensor_3_ = energy_sensor_3; }
  void set_energy_sensor_4(sensor::Sensor *energy_sensor_4) { energy_sensor_4_ = energy_sensor_4; }
  void set_energy_sensor_5(sensor::Sensor *energy_sensor_5) { energy_sensor_5_ = energy_sensor_5; }
  void set_energy_sensor_6(sensor::Sensor *energy_sensor_6) { energy_sensor_6_ = energy_sensor_6; }
  void set_energy_sensor_sum(sensor::Sensor *energy_sensor_sum) { energy_sensor_sum_ = energy_sensor_sum; }
  void set_frequency_sensor(sensor::Sensor *frequency_sensor) { frequency_sensor_ = frequency_sensor; }
  void set_temperature_sensor(sensor::Sensor *temperature_sensor) { temperature_sensor_ = temperature_sensor; }
  void loop() override;

  void update() override;
  void setup() override;
  // void dump_config() override;

 protected:
  process_state m_process_state{PROCESS_DONE};
  template<typename... Ts> friend class ResetEnergyAction;

  sensor::Sensor *voltage_sensor_{nullptr};
  sensor::Sensor *current_sensor_1_{nullptr};
  sensor::Sensor *current_sensor_2_{nullptr};
  sensor::Sensor *current_sensor_3_{nullptr};
  sensor::Sensor *current_sensor_4_{nullptr};
  sensor::Sensor *current_sensor_5_{nullptr};
  sensor::Sensor *current_sensor_6_{nullptr};
  sensor::Sensor *power_sensor_1_{nullptr};
  sensor::Sensor *power_sensor_2_{nullptr};
  sensor::Sensor *power_sensor_3_{nullptr};
  sensor::Sensor *power_sensor_4_{nullptr};
  sensor::Sensor *power_sensor_5_{nullptr};
  sensor::Sensor *power_sensor_6_{nullptr};
  sensor::Sensor *power_sensor_sum_{nullptr};
  sensor::Sensor *energy_sensor_1_{nullptr};
  sensor::Sensor *energy_sensor_2_{nullptr};
  sensor::Sensor *energy_sensor_3_{nullptr};
  sensor::Sensor *energy_sensor_4_{nullptr};
  sensor::Sensor *energy_sensor_5_{nullptr};
  sensor::Sensor *energy_sensor_6_{nullptr};
  sensor::Sensor *energy_sensor_sum_{nullptr};
  sensor::Sensor *frequency_sensor_{nullptr};
  sensor::Sensor *temperature_sensor_{nullptr};

  // 乘以该值以转换为实际 总电量值 (kWh)
  float sum_energy_reference_ = BL0906_CF;

  // 乘以该值以转换为实际 总功率值(W)
  float sum_power_reference_ = BL0906_WATT;

  // 乘以该值以转换为实际功率值(W)
  float power_reference_ = BL0906_PREF;
  // 乘以该值以转换为实际电压值(V)
  float voltage_reference_ = BL0906_UREF;
  // 乘以该值以转换为实际电流值(A)
  float current_reference_ = BL0906_IREF;
  // 乘以该值以转换为实际电量值 (kWh)
  float energy_reference_ = BL0906_EREF;

  float frequency_reference_ = BL0906_FREF;  // 频率转换.Hz

  float temperature_reference_ = BL0906_TREF;  // 内部温度。℃

  static uint32_t to_uint32_t(ube24_t input);

  static int32_t to_int32_t(sbe24_t input);

  // 能量清零设置
  void reset_energy_();

  // 读取数据
  void read_data(const uint8_t address, const float reference, sensor::Sensor *sensor_);
  // 偏置校正
  void Bias_correction(const uint8_t address, const float measurements, const float Correction);
  // 增益调整
  void gain_correction(const uint8_t address, const float measurements, const float Correction,
                       const float coefficient);
  void received_package_(const DataPacket *data) const;

  int addActionCallBack(ActionCallbackFuncPtr ptrFunc);
  void handleActionCallback();
  bool isNeedHandleActionCallback() { return (m_vecActionCallback.size() > 0); }

 private:
  std::vector<ActionCallbackFuncPtr> m_vecActionCallback{};
};

template<typename... Ts> class ResetEnergyAction : public Action<Ts...> {
 public:
  ResetEnergyAction(BL0906 *bl0906) : bl0906_(bl0906) {}

  void play(Ts... x) override {
    this->bl0906_->addActionCallBack(&BL0906::reset_energy_);
    // ESP_LOGI("ResetEnergyAction", "BL0906 addActionCallBack,[reset_energy_]");
  }

 protected:
  BL0906 *bl0906_;
};
}  // namespace bl0906
}  // namespace esphome
