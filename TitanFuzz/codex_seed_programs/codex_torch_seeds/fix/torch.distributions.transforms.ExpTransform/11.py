'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ExpTransform\ntorch.distributions.transforms.ExpTransform(cache_size=0)\n'
import torch
import torch.distributions.transforms as transforms
input_data = torch.rand(2, 3)
exp_transform = transforms.ExpTransform(cache_size=0)
output_data = exp_transform(input_data)
print(output_data)