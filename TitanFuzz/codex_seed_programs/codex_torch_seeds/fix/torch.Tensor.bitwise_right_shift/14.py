'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_right_shift\ntorch.Tensor.bitwise_right_shift(_input_tensor, other)\n'
import torch
in_tensor = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.int32)
print('Input tensor: ', in_tensor)
out_tensor = torch.Tensor.bitwise_right_shift(in_tensor, 2)
print('Output tensor: ', out_tensor)