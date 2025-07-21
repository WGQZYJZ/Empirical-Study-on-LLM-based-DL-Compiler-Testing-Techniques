'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logit\ntorch.Tensor.logit(_input_tensor)\n'
import torch
input_data = torch.randn(5, 3)
output_data = torch.Tensor.logit(input_data)
print('Input data: ', input_data)
print('Output data: ', output_data)