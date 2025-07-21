'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.SoftmaxTransform\ntorch.distributions.transforms.SoftmaxTransform(cache_size=0)\n'
import torch
from torch.distributions.transforms import SoftmaxTransform
data = torch.randn(3, 4)
softmax = SoftmaxTransform(cache_size=0)
print(softmax(data))