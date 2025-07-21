'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.unbind\ntorch.Tensor.unbind(_input_tensor, dim=0)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = torch.Tensor.unbind(input_tensor, dim=0)
print(result)