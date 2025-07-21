'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.clamp\ntorch.Tensor.clamp(_input_tensor, min=None, max=None)\n'
import torch
input_data = torch.rand(100, 100)
output_data = input_data.clamp(min=0.5, max=0.7)
print(output_data)