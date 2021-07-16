# Model Optimization

- [Task](#Task)
- [Dataset](#dataset)
  - [TACO](#taco)
  - [Evaluation](#evaluation)
- [Training details](#training-details)
- [Result](#result)
- [Usage](#usage)
  - [Install requirements](#install-requirements)
  - [Train](#train)
  - [Tune](#tune)
  - [Inference](#inference)

---

## Task
최근들어 여러 산업에서 인공지능을 이용해 그동안 해결하지 못 했던 문제들을 풀려는 노력을 하고 있습니다. 대표적인 태스크로는 쓰레기의 재활용 가능 여부을 판단하는 인공지능 쓰레기통이 있습니다. 이를 위해서는 쓰레기 이미지를 분류하는 모델이 탑재되어야 합니다. 하지만 분류만 잘 한다고 해서 사용할 수 있는 것은 아닙니다. 로봇 내부 시스템에 탑재되어 즉각적으로 쓰레기를 분류할 수 있어야만 실제로 사용이 될 수 있습니다.

본 프로젝트(2021.05.24 - 2021.06.18)에서는 분리수거 로봇의 기초 기술인 쓰레기 이미지 분류기를 만들면서 실제로 로봇에 탑재될 만큼 작고 계산량이 적은 모델을 만들었습니다. Base model로는 [MobileNetV2](https://arxiv.org/abs/1801.04381), [EfficientNet](https://arxiv.org/abs/1905.11946) 를 사용했고, Optuna AutoML로 모델 경량화 및 최적화를 진행했습니다.

## Dataset
### TACO
Segmentation / Object detecion task를 풀기 위해 제작된 COCO format의 재활용 쓰레기 데이터인 TACO 데이터셋을 사용합니다. 단순한 Classification 문제로 설정하기 위해 TACO의 Bounding box를 crop한 데이터를 사용했습니다.

![TACO](https://user-images.githubusercontent.com/77161691/125893628-6319352f-b26c-4b65-a7ea-32fff671030e.png)

TACO dataset은 총 9개의 category로 이루어져 있습니다.

```python
category = ["Battery", "Clothing", "Glass", "Metal", "Paper", "Paperpack", "Plastic", "Plasticbag", "Styrofoam"]
```

본 프로젝트에서 사용하는 데이터의 분포는 아래와 같습니다.

![Category](https://user-images.githubusercontent.com/77161691/125894094-e03d1246-78fe-44c4-a9c2-2cfe115b5f8a.png)

- train dataset: 총 32,599장 (label 포함)
- test dataset: 총 8,159장 (label 미포함)

### Evaluation
본 프로젝트에서는 `f1-score`와 `MACs`의 두 가지 척도를 도입했습니다. `f1-score`는 이미지의 추론된 라벨과 실제 라벨이 얼마나 일치하는지를 측정하는 `모델 성능`에 관한 지표입니다. `MACs`는 모델의 총 연산량을 나타내는 `모델 경량화`에 관한 지표입니다.

일정 `f1-score` 이상을 만족한 후에는 로봇에 탑재될 수 있을 만큼 `MACs`를 줄이는 것이 중요합니다. 현실에서의 효용성 평가를 위해 아래와 같이 `total score`로 모델을 평가했습니다.

![Score](https://user-images.githubusercontent.com/77161691/125894785-5b0df7e9-9c91-4fa9-b8c4-735c9e00abd9.png)

## Training Details
| Model | Image Size | Batch Size | Epochs | Initial LR | Train & Optimize Time |
| :--- | ---: | ---: | ---: | ---: | ---: |
| `Efficientnet` | 70 | 64 | 500 | 0.2 | 5d |
| `MobileNetV2` | 224 | 256 | 200 | 0.1 | 2d |

- **P40**을 이용하여 학습하였습니다.

## Result
| Model | Total Score | F1 Score | MACs |
| --- | ---: | ---: | ---: |
| [EfficientNet](https://arxiv.org/abs/1905.11946) | 0.7064 | 0.5275 | 4670834 |
| [MobileNetV2](https://arxiv.org/abs/1801.04381) | 9.9846 | 0.6525 | 135389513 |

## Usage
### Install requirements
Please refer to `environment.yml`

### Train
```
python train.py
```
Please refer to `train.py` for train arguments.

### Tune
```
python tune.py
```
Please refer to `tune.py` for evaluation arguments.

### Inference
```
python inference.py
```
Please refer to `inference.py` for inference arguments.

---
#### Docs
- https://arxiv.org/abs/1905.11946
- https://arxiv.org/abs/1801.04381
- https://optuna.readthedocs.io/en/stable/tutorial/index.html
- https://arxiv.org/abs/1909.13719v2
