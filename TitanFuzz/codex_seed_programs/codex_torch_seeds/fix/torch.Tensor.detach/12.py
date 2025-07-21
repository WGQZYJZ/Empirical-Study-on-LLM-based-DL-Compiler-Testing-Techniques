'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.detach\ntorch.Tensor.detach(_input_tensor, )\n'
import torch
input_tensor = torch.rand(size=(3, 3))
detached_tensor = torch.Tensor.detach(input_tensor)
print('input_tensor is: ', input_tensor)
print('detached_tensor is: ', detached_tensor)