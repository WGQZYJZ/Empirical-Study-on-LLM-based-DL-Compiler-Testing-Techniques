'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isclose\ntorch.Tensor.isclose(_input_tensor, other, rtol=1e-05, atol=1e-08, equal_nan=False)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
other = torch.tensor([[1, 2, 3], [4, 5, 6]])
result = torch.Tensor.isclose(input_tensor, other)
print(result)