'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.positive\ntorch.Tensor.positive(_input_tensor)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
print(input_data.positive())
print(input_data.neg())
print(input_data.abs())
print(input_data.sign())
print(input_data.clamp(min=0.5))
print(input_data.clamp(min=0.5, max=0.8))
print(input_data.clamp_min(min=0.5))
print(input_data.clamp_max(max=0.8))