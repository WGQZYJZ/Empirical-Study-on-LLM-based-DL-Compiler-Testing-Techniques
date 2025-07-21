'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log10\ntorch.Tensor.log10(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3)
print('The input tensor: ', input_tensor)
output_tensor = input_tensor.log10()
print('The output tensor: ', output_tensor)