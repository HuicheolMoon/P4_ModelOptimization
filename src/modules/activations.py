# Custom activation to work with onnx.

import torch
import torch.nn as nn
from torch.nn import functional as F


def hard_sigmoid(x: torch.Tensor, inplace: bool = False):
    """Hard sigmoid."""
    if inplace:
        return x.add_(3.0).clamp_(0.0, 6.0).div_(6.0)
    else:
        return F.relu6(x + 3.0) / 6.0


class HardSigmoid(nn.Module):
    """Hard sigmoid."""

    def __init__(self, inplace: bool = False):
        """Initialize."""
        super().__init__()
        self.inplace = inplace

    def forward(self, x: torch.Tensor):
        """Forward."""
        return hard_sigmoid(x, self.inplace)


def hard_swish(x: torch.Tensor, inplace: bool = False):
    """Hard swish."""
    inner = F.relu6(x + 3.0).div_(6.0)
    return x.mul_(inner) if inplace else x.mul(inner)


class HardSwish(nn.Module):
    """Custom hardswish to work with onnx."""

    def __init__(self, inplace: bool = False):
        """Initialize."""
        super().__init__()
        self.inplace = inplace

    def forward(self, x: torch.Tensor):
        """Forward."""
        return hard_swish(x, self.inplace)


def swish(x: torch.Tensor, inplace: bool = False):
    """Swish - Described originally as SiLU (https://arxiv.org/abs/1702.03118v3)
    and also as Swish (https://arxiv.org/abs/1710.05941).
    TODO Rename to SiLU with addition to PyTorch
    Adopted to handle onnx conversion
    """
    return x.mul_(x.sigmoid()) if inplace else x.mul(x.sigmoid())


class Swish(nn.Module):
    """Swish."""

    def __init__(self, inplace: bool = False):
        """Initialize."""
        super().__init__()
        self.inplace = inplace

    def forward(self, x: torch.Tensor):
        """Forward."""
        return swish(x, self.inplace)
