'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.empty_strided\ntorch.empty_strided(size, stride, *, dtype=None, layout=None, device=None, requires_grad=False, pin_memory=False)\n'
import torch
input_data = torch.randn(20, 16, 50, 32)
print('input_data.shape: ', input_data.shape)
output = torch.empty_strided(size=(20, 16, 50, 32), stride=(1, 1, 1, 1))
print('output.shape: ', output.shape)