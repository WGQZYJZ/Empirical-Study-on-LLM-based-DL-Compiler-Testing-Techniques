'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.frac\ntorch.Tensor.frac(_input_tensor)\n'
import torch
input_data = torch.randn(3, 4)
frac_data = input_data.frac()
print('input_data is:', input_data)
print('frac_data is:', frac_data)