'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to\ntorch.Tensor.to(_input_tensor, *args, **kwargs)\n'
import torch
import torch
data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = data.to(dtype=torch.float32)
print(result)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to\ntorch.Tensor.to(_input_tensor, *args, **kwargs)\n'
import torch
import torch
data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = data.to(device=torch.device('cuda:0'))
print(result)