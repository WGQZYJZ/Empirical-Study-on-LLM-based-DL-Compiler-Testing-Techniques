'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.StickBreakingTransform\ntorch.distributions.transforms.StickBreakingTransform(cache_size=0)\n'
import torch
from torch.distributions.transforms import StickBreakingTransform
num_categories = 3
batch_size = 2
stick_breaking_transform = StickBreakingTransform(cache_size=0)
print('stick_breaking_transform = {}'.format(stick_breaking_transform))
x = torch.rand(batch_size, num_categories)
print('x = {}'.format(x))
y = stick_breaking_transform.inv(x)
print('y = {}'.format(y))