'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cos_\ntorch.Tensor.cos_(_input_tensor)\n'
import torch
input_data = torch.randn(3, 3)
print('Input data: ', input_data)
output_data = input_data.cos_()
print('Output data: ', output_data)