'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.equal\ntorch.Tensor.equal(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
other = torch.tensor([[1, 2], [3, 4]])
result = torch.Tensor.equal(input_tensor, other)
print(result)