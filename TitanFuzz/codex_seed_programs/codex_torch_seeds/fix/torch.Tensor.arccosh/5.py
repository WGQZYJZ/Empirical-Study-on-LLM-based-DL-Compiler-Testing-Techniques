'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arccosh\ntorch.Tensor.arccosh(_input_tensor)\n'
import torch
input_data = torch.randn(10)
print('The input data is: ', input_data)
print('The result of arccosh is: ', input_data.arccosh())