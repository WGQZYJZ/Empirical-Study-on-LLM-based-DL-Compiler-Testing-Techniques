'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ExpTransform\ntorch.distributions.transforms.ExpTransform(cache_size=0)\n'
import torch
from torch.distributions.transforms import ExpTransform
input_data = torch.rand(2, 3)
print('Input data: \n{}'.format(input_data))
exp_transform = ExpTransform()
output_data = exp_transform(input_data)
print('Output data: \n{}'.format(output_data))