'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccos\ntorch.Tensor.arccos(_input_tensor)\n'
import torch
input_data = torch.randn(1, 3)
print(input_data)
output = torch.Tensor.arccos(input_data)
print(output)