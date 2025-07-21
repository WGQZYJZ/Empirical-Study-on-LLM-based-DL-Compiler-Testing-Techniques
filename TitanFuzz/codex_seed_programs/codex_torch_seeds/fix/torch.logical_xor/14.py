'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_xor\ntorch.logical_xor(input, other, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 1], [1, 0], [0, 1], [0, 0]], dtype=torch.float)
output = torch.logical_xor((input_data[:, 0] > 0), (input_data[:, 1] > 0))
print(output)