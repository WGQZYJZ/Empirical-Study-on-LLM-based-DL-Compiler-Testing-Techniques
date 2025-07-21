'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummax\ntorch.Tensor.cummax(_input_tensor, dim)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
cummax_tensor = input_tensor.cummax(dim=1)
print(cummax_tensor)