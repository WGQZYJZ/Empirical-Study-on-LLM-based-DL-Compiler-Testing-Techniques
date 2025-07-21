'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.maximum\ntorch.Tensor.maximum(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
other = torch.tensor([[5, 6], [7, 8]])
maximum = torch.Tensor.maximum(input_tensor, other)
print(maximum)