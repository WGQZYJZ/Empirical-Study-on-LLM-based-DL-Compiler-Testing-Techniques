'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.SigmoidTransform\ntorch.distributions.transforms.SigmoidTransform(cache_size=0)\n'
import torch
import torch.distributions.transforms as transforms
input_data = torch.rand(2, 3)
sigmoid_transform = transforms.SigmoidTransform(cache_size=0)
print(sigmoid_transform(input_data))
print(sigmoid_transform.inv(sigmoid_transform(input_data)))