'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.acos\ntorch.acos(input, *, out=None)\n'
import torch
input_tensor = ((torch.rand(4, 4) * 20) - 10)
print('Input Tensor: ', input_tensor)
acos_tensor = torch.acos(input_tensor)
print('Result of torch.acos: ', acos_tensor)