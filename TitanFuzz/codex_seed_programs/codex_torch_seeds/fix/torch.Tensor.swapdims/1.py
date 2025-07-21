'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapdims\ntorch.Tensor.swapdims(_input_tensor, dim0, dim1)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
print(input_tensor)
swapdims_tensor = torch.Tensor.swapdims(input_tensor, 0, 2)
print(swapdims_tensor)