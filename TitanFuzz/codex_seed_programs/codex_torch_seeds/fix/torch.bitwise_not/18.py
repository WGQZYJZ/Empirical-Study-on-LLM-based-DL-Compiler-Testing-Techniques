'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_not\ntorch.bitwise_not(input, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 0], [0, 1]], dtype=torch.bool)
print(torch.bitwise_not(input_data))