'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.greater_equal\ntorch.Tensor.greater_equal(_input_tensor, other)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
other = torch.Tensor([[1, 2, 3], [4, 5, 6]])
result = torch.Tensor.greater_equal(input_tensor, other)
print(result)