'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.maximum\ntorch.Tensor.maximum(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(5)
other = torch.rand(5)
maximum_result = torch.Tensor.maximum(input_tensor, other)
print(maximum_result)