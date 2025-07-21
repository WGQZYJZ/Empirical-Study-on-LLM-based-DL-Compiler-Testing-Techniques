'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frac_\ntorch.Tensor.frac_(_input_tensor)\n'
import torch
input_data = torch.rand(1, 3, 3)
print('Input data: ', input_data)
print('Output data: ', input_data.frac_())