# Holosoma G1 FastSAC Slope Robustness

Model: `/home/smp/projects/holosoma/logs/hv-g1-manager/20260508_090804-rtx3080_1024bs2048_isaacgym_fastsac_defaultmix_resume20k_to_50000-locomotion/model_0050000.onnx`

Overall trial success rate: `0.472`

Training used IsaacGym on default mixed terrain with RTX-3080-safe parameters:
`num_envs=1024`, `batch_size=2048`, `compile=False`.

The final evaluated checkpoint is the completed 50k ONNX export.

Latest parsed training metrics: iteration `50000.0000`,
linear tracking `1.0139`, angular tracking `0.8756`.

IsaacGym was stable under WSL2 with `/usr/lib/wsl/lib` in `LD_LIBRARY_PATH`.
MJWarp was not used for the final policy because it failed earlier on default mixed terrain.

![Training metrics](figures/training_metrics.png)

![Slope success heatmap](figures/slope_success_heatmap.png)

![Max grade polar chart](figures/max_grade_polar.png)

## Direction Thresholds

| Uphill direction deg | Max passing grade | Slope angle deg |
|---:|---:|---:|
| 0.0 | 0.05 | 2.9 |
| 22.5 | 0.05 | 2.9 |
| 45.0 | 0.05 | 2.9 |
| 67.5 | 0.10 | 5.7 |
| 90.0 | 0.20 | 11.3 |
| 112.5 | 0.25 | 14.0 |
| 135.0 | 0.25 | 14.0 |
| 157.5 | 0.20 | 11.3 |
| 180.0 | 0.25 | 14.0 |
| 202.5 | 0.15 | 8.5 |
| 225.0 | 0.20 | 11.3 |
| 247.5 | 0.25 | 14.0 |
| 270.0 | 0.20 | 11.3 |
| 292.5 | 0.20 | 11.3 |
| 315.0 | 0.15 | 8.5 |
| 337.5 | 0.10 | 5.7 |

## Sample Successes and Failures

### Sample Slope Successes

| Outcome | Direction deg | Grade | Angle deg | Reason | vx m/s | progress m | yaw rad/s | Replay args |
|---|---:|---:|---:|---|---:|---:|---:|---|
| success | 180.0 | 0.25 | 14.0 | passed | 0.736 | 5.614 | 0.210 | `slope --direction-deg 180 --grade 0.25` |
| success | 135.0 | 0.25 | 14.0 | passed | 0.684 | 4.513 | 0.230 | `slope --direction-deg 135 --grade 0.25` |
| success | 112.5 | 0.25 | 14.0 | passed | 0.408 | 3.453 | 0.195 | `slope --direction-deg 112.5 --grade 0.25` |
| success | 247.5 | 0.25 | 14.0 | passed | 0.264 | 2.980 | 0.256 | `slope --direction-deg 247.5 --grade 0.25` |
| success | 180.0 | 0.20 | 11.3 | passed | 0.675 | 5.090 | 0.172 | `slope --direction-deg 180 --grade 0.2` |
| success | 225.0 | 0.20 | 11.3 | passed | 0.628 | 4.425 | 0.179 | `slope --direction-deg 225 --grade 0.2` |

### Sample Slope Failures

| Outcome | Direction deg | Grade | Angle deg | Reason | vx m/s | progress m | yaw rad/s | Replay args |
|---|---:|---:|---:|---|---:|---:|---:|---|
| failure | 180.0 | 0.40 | 21.8 | reset/fall, slow vx, low progress | 0.000 | 0.079 | 0.000 | `slope --direction-deg 180 --grade 0.4` |
| failure | 337.5 | 0.40 | 21.8 | reset/fall, slow vx, low progress | 0.000 | 0.022 | 0.000 | `slope --direction-deg 337.5 --grade 0.4` |
| failure | 22.5 | 0.35 | 19.3 | reset/fall, slow vx, low progress | 0.000 | -0.610 | 0.000 | `slope --direction-deg 22.5 --grade 0.35` |
| failure | 202.5 | 0.35 | 19.3 | reset/fall, slow vx, low progress | -0.091 | 0.763 | 0.069 | `slope --direction-deg 202.5 --grade 0.35` |
| failure | 157.5 | 0.35 | 19.3 | reset/fall, slow vx, low progress, yaw drift | -1.215 | 0.333 | 3.698 | `slope --direction-deg 157.5 --grade 0.35` |
| failure | 180.0 | 0.30 | 16.7 | reset/fall, low progress, yaw drift | 0.363 | 0.558 | 1.389 | `slope --direction-deg 180 --grade 0.3` |


## Viewer Replay

From the repository root:

```bash
source scripts/source_isaacgym_setup.sh
export LD_LIBRARY_PATH=/usr/lib/wsl/lib:${LD_LIBRARY_PATH:-}
python reports/slope_robustness_50k/replay_eval_case.py slope --sample failure
```

Other examples:

```bash
python reports/slope_robustness_50k/replay_eval_case.py slope --sample success
python reports/slope_robustness_50k/replay_eval_case.py slope --direction-deg 0 --grade 0.10
python reports/slope_robustness_50k/replay_eval_case.py stress --sample failure
python reports/slope_robustness_50k/replay_eval_case.py stress --terrain-type stairs_up --magnitude 0.08
```

## Additional Terrain Stress Tests

Overall terrain-stress trial success rate: `0.722`.

![Additional terrain stress tests](figures/terrain_stress_tests.png)

| Terrain type | Max passing magnitude | Unit | Passing cells | Tested cells |
|---|---:|---|---:|---:|
| blocks | 0.120 | m_height | 5 | 6 |
| cross_gap | 0.150 | m_width | 3 | 6 |
| pits | 0.100 | m_depth | 5 | 6 |
| rough | 0.100 | m_amp | 6 | 6 |
| stairs_down | 0.100 | m_step | 5 | 6 |
| stairs_up | 0.040 | m_step | 2 | 6 |

### Sample Terrain-Stress Successes

| Outcome | Terrain | Magnitude | Unit | Reason | vx m/s | progress m | yaw rad/s | Replay args |
|---|---|---:|---|---|---:|---:|---:|---|
| success | stairs_up | 0.040 | m_step | passed | 0.330 | 2.237 | 0.072 | `stress --terrain-type stairs_up --magnitude 0.04` |
| success | stairs_up | 0.020 | m_step | passed | 0.381 | 2.717 | 0.072 | `stress --terrain-type stairs_up --magnitude 0.02` |
| success | stairs_down | 0.100 | m_step | passed | 0.422 | 4.307 | 0.506 | `stress --terrain-type stairs_down --magnitude 0.1` |
| success | stairs_down | 0.080 | m_step | passed | 0.533 | 4.265 | 0.136 | `stress --terrain-type stairs_down --magnitude 0.08` |
| success | stairs_down | 0.060 | m_step | passed | 0.536 | 4.239 | 0.110 | `stress --terrain-type stairs_down --magnitude 0.06` |
| success | stairs_down | 0.040 | m_step | passed | 0.545 | 4.221 | 0.092 | `stress --terrain-type stairs_down --magnitude 0.04` |

### Sample Terrain-Stress Failures

| Outcome | Terrain | Magnitude | Unit | Reason | vx m/s | progress m | yaw rad/s | Replay args |
|---|---|---:|---|---|---:|---:|---:|---|
| failure | cross_gap | 0.200 | m_width | reset/fall | 0.488 | 2.071 | 0.351 | `stress --terrain-type cross_gap --magnitude 0.2` |
| failure | cross_gap | 0.300 | m_width | reset/fall | 0.483 | 2.097 | 0.350 | `stress --terrain-type cross_gap --magnitude 0.3` |
| failure | cross_gap | 0.400 | m_width | reset/fall | 0.448 | 2.270 | 0.497 | `stress --terrain-type cross_gap --magnitude 0.4` |
| failure | stairs_up | 0.120 | m_step | slow vx, low progress | 0.006 | -0.243 | 0.132 | `stress --terrain-type stairs_up --magnitude 0.12` |
| failure | stairs_down | 0.120 | m_step | yaw drift | 0.579 | 4.555 | 0.747 | `stress --terrain-type stairs_down --magnitude 0.12` |
| failure | pits | 0.120 | m_depth | slow vx, low progress | 0.216 | 1.732 | 0.124 | `stress --terrain-type pits --magnitude 0.12` |


