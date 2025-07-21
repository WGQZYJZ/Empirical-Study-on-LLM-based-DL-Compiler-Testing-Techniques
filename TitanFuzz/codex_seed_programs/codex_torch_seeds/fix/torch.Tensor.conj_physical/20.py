'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.conj_physical\ntorch.Tensor.conj_physical(_input_tensor)\n'
import torch
input_tensor = torch.rand(4, 4)
print('input_tensor: {}'.format(input_tensor))
conj_physical_tensor = torch.Tensor.conj_physical(input_tensor)
print('conj_physical_tensor: {}'.format(conj_physical_tensor))