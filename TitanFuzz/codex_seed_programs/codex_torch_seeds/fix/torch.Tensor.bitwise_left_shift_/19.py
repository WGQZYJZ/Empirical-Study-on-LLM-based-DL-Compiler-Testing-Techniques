'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift_\ntorch.Tensor.bitwise_left_shift_(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(4, 4)
other = torch.ones(4, 4)
torch.Tensor.bitwise_left_shift_(input_tensor, other)
print(input_tensor)