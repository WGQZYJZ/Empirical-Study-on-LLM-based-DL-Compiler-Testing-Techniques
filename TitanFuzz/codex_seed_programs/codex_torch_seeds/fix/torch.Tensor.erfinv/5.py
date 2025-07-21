'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.erfinv\ntorch.Tensor.erfinv(_input_tensor)\n'
import torch
input_tensor = torch.rand(10)
result = torch.Tensor.erfinv(input_tensor)
print(result)