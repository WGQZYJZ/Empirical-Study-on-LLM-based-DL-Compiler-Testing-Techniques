'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.renorm_\ntorch.Tensor.renorm_(_input_tensor, p, dim, maxnorm)\n'
import torch
input_tensor = torch.arange(0, 6).view(2, 3)
print('Tensor: \n', input_tensor)
torch.Tensor.renorm_(input_tensor, p=1, dim=1, maxnorm=5)
print('Renormed tensor: \n', input_tensor)