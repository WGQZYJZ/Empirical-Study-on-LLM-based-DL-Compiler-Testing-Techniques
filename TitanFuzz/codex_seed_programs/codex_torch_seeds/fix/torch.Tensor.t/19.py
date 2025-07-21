'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.t\ntorch.Tensor.t(_input_tensor)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
print(input_data.t())
print(input_data.transpose(0, 1))