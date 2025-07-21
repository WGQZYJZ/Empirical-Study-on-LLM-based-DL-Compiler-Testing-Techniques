'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.conj_physical_\ntorch.Tensor.conj_physical_(_input_tensor)\n'
import torch
input_tensor = torch.randn(5, 5)
print('Input Tensor: ', input_tensor)
torch.Tensor.conj_physical_(input_tensor)
print('Output Tensor: ', input_tensor)