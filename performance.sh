#!/usr/bin/env bash
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
echo 0 | tee /sys/devices/system/cpu/cpu*/power/energy_perf_bias
