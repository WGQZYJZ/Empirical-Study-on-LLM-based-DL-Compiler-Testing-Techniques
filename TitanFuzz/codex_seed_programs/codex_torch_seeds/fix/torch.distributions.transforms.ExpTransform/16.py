'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ExpTransform\ntorch.distributions.transforms.ExpTransform(cache_size=0)\n'
import torch
from torch.distributions.transforms import ExpTransform
x = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
exp_transform = ExpTransform()
print('The result of ExpTransform is: ', exp_transform(x))