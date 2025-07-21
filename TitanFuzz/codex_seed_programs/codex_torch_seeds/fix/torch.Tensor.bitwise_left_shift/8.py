'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift\ntorch.Tensor.bitwise_left_shift(_input_tensor, other)\n'
import torch
input_tensor = torch.randn(5, 3)
print('input_tensor: ', input_tensor)
result_tensor = input_tensor.bitwise_left_shift(2)
print('result_tensor: ', result_tensor)