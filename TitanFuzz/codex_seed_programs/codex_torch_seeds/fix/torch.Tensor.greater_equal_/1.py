'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.greater_equal_\ntorch.Tensor.greater_equal_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(5, 3), dtype=torch.float)
result = torch.Tensor.greater_equal_(input_tensor, 5)
print(input_tensor)
print(result)