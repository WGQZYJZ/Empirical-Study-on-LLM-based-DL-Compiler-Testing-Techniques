'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gt\ntorch.Tensor.gt(_input_tensor, other)\n'
import torch
input_data = torch.randn(3, 3)
print(input_data)
print(input_data.gt(0))