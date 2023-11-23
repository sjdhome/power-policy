#!/usr/bin/env bash
echo powersave | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
echo 15 | tee /sys/devices/system/cpu/cpu*/power/energy_perf_bias
