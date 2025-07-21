'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ones\ntorch.ones(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
size = [2, 3]
output = torch.ones(size)
print('The output tensor: ', output)
print('The shape of output tensor: ', output.shape)
print('The data type of output tensor: ', output.dtype)
print('The device of output tensor: ', output.device)
print('The requires_grad of output tensor: ', output.requires_grad)