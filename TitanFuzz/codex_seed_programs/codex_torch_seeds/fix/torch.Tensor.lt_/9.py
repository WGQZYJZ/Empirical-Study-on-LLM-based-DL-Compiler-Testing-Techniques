'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lt_\ntorch.Tensor.lt_(_input_tensor, other)\n'
import torch
data = torch.tensor([1, 2, 3])
print(data)
print(data.lt_(2))
print(data.lt_(1))