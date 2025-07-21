'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frac\ntorch.Tensor.frac(_input_tensor)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data: ', input_data)
output_data = input_data.frac()
print('Output data: ', output_data)