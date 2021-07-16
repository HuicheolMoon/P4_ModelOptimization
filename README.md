# Dialogue State Tracking

- [Task](#Task)
- [Dataset](#dataset)
  - [Wizard of Seoul](#wizard-of-seoul)
  - [Evaluation](#evaluation)
- [Training details](#training-details)
- [Result](#result)
- [Usage](#usage)
  - [Install requirements](#install-requirements)
  - [Train](#train)
  - [Inference](#inference)
  - [Evaluation](#evaluation)

---

## Task
`목적 지향형 대화(Task-Oriented Dialogue)`에서는 유저가 미리 정의된 시나리오 안에서 특정 목적을 수행하기 위해 대화를 진행한다고 가정합니다. 그리고 `대화 상태 추적(Dialogue State Tracking)`은 목적 지향형 대화의 중요한 하위 태스크 중 하나입니다. 유저와의 대화에서 미리 시나리오에 의해 정의된 정보인 `Slot`과 매 턴마다 그에 속할 수 있는 `Value`의 집합인 `Dialogue State(대화 상태)`를 매 턴마다 추론해야 합니다.

![DST](https://user-images.githubusercontent.com/77161691/125183603-c974c200-e252-11eb-9320-33b11d66a1e5.png)

본 프로젝트(2021.04.26 - 2021.05.23)에서는 유저와의 대화에서 기정의된 시나이로의 대화 상태를 매 턴마다 추론하는 모델을 학습시켰습니다. 그리고 시나리오에 대해 매 턴마다 알맞은 대화 상태를 예측했습니다. Base model로는 [TRADE](https://github.com/jasonwu0731/trade-dst), [SUMBT](https://github.com/SKTBrain/SUMBT) 를 사용했습니다.

## Dataset
### Wizard of Seoul
Wizard of Seoul은 아래와 같은 형식을 가지는 대화 데이터의 리스트입니다.

![Wizard of Seoul](https://user-images.githubusercontent.com/77161691/125186631-6e4cca80-e266-11eb-8137-7c8a4a801258.png)

- train dataset: 7000개의 대화 (label 포함)
- test dataset: 1000개의 대화 (label 미포함)

### Evaluation
본 프로젝트에서는 `Joint Goal Accuracy`와 `Slot Accuracy`, 그리고 `Slot F1 Score`의 세 가지 척도로 모델을 평가했습니다. `Joint Goal Accuracy`는 추론된 `Dialogue State`와 실제 `Dialogue State`가 완벽히 일치하는지를 측정합니다. `Slot Accuracy`와 `Slot F1 Score`는 턴 레벨의 측정이 아닌 그 원소인 (Slot, Value) pair에 대한 Accuracy를 측정합니다. `Joint Goal Accuracy`가 `Slot Accuracy`와 `Slot F1 Score` 보다 우선되는 기준입니다.

## Training Details
| Model | Batch Size | epochs | LR | Train Time |
| :--- | ---: | ---: | ---: | ---: |
| `TRADE` | 8 | 50 | 5e-4 | 43h |
| `SUMBT` | 8 | 30 | 5e-5 | 30h |

- **V100**을 이용하여 학습하였습니다.

## Result
| Model | Joint Goal Accuracy | Slot Accuracy | Slot F1 Score |
| --- | ---: | ---: | ---: |
| [TRADE](https://github.com/jasonwu0731/trade-dst) | 65.64 | 98.93 | 95.63 |
| [SUMBT](https://github.com/SKTBrain/SUMBT) | 59.57 | 98.66 | 93.92 |

## Usage
### Install requirements
```
pip install -r requirements.txt
```

### Train
```
python train.py
```
Please refer to `train.py` for train arguments.

### Inference
```
python inference.py
```
Please refer to `inference.py` for inference arguments.

### Evaluation
```
python evaluation.py
```
Please refer to `evaluation.py` for evaluation arguments.

---
#### Docs
- https://github.com/jasonwu0731/trade-dst
- https://github.com/SKTBrain/SUMBT
- https://github.com/clovaai/som-dst
- https://github.com/zengyan-97/Transformer-DST
- https://paperswithcode.com/sota/multi-domain-dialogue-state-tracking-on

#### License
CC-BY-SA
