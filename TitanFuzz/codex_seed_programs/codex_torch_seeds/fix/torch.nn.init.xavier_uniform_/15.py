'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_uniform_\ntorch.nn.init.xavier_uniform_(tensor, gain=1.0)\n'
import torch
input_size = 5
output_size = 3
input_data = torch.randn(input_size, output_size)
torch.nn.init.xavier_uniform_(input_data, gain=1.0)
print(input_data)