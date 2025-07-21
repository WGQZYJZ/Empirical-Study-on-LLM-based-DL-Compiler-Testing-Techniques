'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.erfc_\ntorch.Tensor.erfc_(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
torch.Tensor.erfc_(input_tensor)
print('Input Tensor: ', input_tensor)