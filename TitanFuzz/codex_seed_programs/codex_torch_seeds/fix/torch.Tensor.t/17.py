'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.t\ntorch.Tensor.t(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
print(input_tensor)
result_tensor = input_tensor.t()
print(result_tensor)