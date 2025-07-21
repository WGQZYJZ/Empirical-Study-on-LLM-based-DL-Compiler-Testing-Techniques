'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softsign\ntorch.nn.Softsign()\n'
import torch
input_tensor = torch.randn(3, 4)
print('Input Tensor: ', input_tensor)
output_tensor = torch.nn.Softsign()(input_tensor)
print('Output Tensor: ', output_tensor)