'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sigmoid\ntorch.sigmoid(input, *, out=None)\n'
import torch
input_data = torch.tensor([[0.1, 0.2, 0.3, 0.4]])
output = torch.sigmoid(input_data)
print(output)