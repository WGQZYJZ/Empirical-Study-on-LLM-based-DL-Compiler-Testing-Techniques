'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tensor_split\ntorch.Tensor.tensor_split(_input_tensor, indices_or_sections, dim=0)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(input_tensor)
result = torch.Tensor.tensor_split(input_tensor, 2, dim=1)
print(result)