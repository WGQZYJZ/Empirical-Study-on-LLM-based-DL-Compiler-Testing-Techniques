'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_uniform_\ntorch.nn.init.xavier_uniform_(tensor, gain=1.0)\n'
import torch
input_size = 10
output_size = 20
input = torch.rand(input_size, output_size)
print(input)
torch.nn.init.xavier_uniform_(input)
print(input)