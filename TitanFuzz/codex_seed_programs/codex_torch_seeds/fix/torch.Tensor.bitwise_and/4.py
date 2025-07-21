'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_and\ntorch.Tensor.bitwise_and(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[0, 1, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0]])
other = torch.tensor([[1, 1, 0, 0], [1, 0, 1, 0], [1, 1, 0, 0]])
result = torch.Tensor.bitwise_and(input_tensor, other)
print(result)