'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mul\ntorch.mul(input, other, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
print(input_data)
print(torch.mul(input_data, input_data))
print(torch.mul(input_data, input_data).shape)