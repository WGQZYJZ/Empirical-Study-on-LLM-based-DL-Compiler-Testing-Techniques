'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor\ntorch.floor(input, *, out=None)\n'
import torch
input_data = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
output_data = torch.floor(input_data)
print(output_data)