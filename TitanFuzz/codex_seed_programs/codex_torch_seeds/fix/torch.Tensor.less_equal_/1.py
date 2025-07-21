'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.less_equal_\ntorch.Tensor.less_equal_(_input_tensor, other)\n'
import torch
input_tensor = torch.arange(0, 10)
output_tensor = input_tensor.less_equal_(5)
print('output_tensor: ', output_tensor)