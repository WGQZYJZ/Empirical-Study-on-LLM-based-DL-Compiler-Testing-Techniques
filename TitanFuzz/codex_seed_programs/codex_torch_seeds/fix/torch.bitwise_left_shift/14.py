'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_left_shift\ntorch.bitwise_left_shift(input, other, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 1, 1], [1, 1, 1]], dtype=torch.int8)
other_data = torch.tensor([[1, 1, 1], [1, 1, 1]], dtype=torch.int8)
torch.bitwise_left_shift(input_data, other_data)