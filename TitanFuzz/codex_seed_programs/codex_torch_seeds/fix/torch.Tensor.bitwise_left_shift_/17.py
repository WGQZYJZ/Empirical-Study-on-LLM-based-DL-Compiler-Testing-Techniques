'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift_\ntorch.Tensor.bitwise_left_shift_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 0, 1, 1], [0, 0, 1, 1]])
other = torch.tensor([[1, 0, 1, 1], [0, 0, 1, 1]])
torch.Tensor.bitwise_left_shift_(input_tensor, other)