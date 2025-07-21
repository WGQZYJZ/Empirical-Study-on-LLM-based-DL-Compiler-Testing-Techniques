'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mm\ntorch.Tensor.mm(_input_tensor, mat2)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
mat2 = torch.tensor([[1, 2], [3, 4], [5, 6]])
result = torch.Tensor.mm(_input_tensor, mat2)
print(result)