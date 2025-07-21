'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_right_shift\ntorch.Tensor.bitwise_right_shift(_input_tensor, other)\n'
import torch
input_tensor = torch.arange(0, 10, 1, dtype=torch.int32)
print('input_tensor = \n', input_tensor)
right_shift_tensor = torch.Tensor.bitwise_right_shift(input_tensor, 2)
print('right_shift_tensor = \n', right_shift_tensor)