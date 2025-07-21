'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.slogdet\ntorch.Tensor.slogdet(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 2)
slogdet = input_tensor.slogdet()
print('slogdet: ', slogdet)