from clloader.datasets.base import (
    BaseDataset, ImageFolderDataset, InMemoryDataset, PyTorchDataset
)
from clloader.datasets.imagenet import ImageNet100, ImageNet1000
from clloader.datasets.pytorch import CIFAR10, CIFAR100, MNIST, FashionMNIST
from clloader.datasets.transformed import PermutedMNIST

# yapf: disable
__all__ = [
    BaseDataset,
    PyTorchDataset,
    InMemoryDataset,
    ImageFolderDataset,
    CIFAR10,
    CIFAR100,
    MNIST,
    FashionMNIST,
    ImageNet100,
    ImageNet1000,
    PermutedMNIST
]