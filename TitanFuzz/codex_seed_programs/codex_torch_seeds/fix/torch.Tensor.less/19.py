'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.less\ntorch.Tensor.less(_input_tensor, other)\n'
import torch
input_tensor = torch.randn((2, 3))
output_tensor = input_tensor.less(0)
print('The input tensor is:', input_tensor)
print('The output tensor is:', output_tensor)