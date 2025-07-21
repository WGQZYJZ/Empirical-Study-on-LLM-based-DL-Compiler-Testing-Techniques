'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_normal_\ntorch.nn.init.xavier_normal_(tensor, gain=1.0)\n'
import torch
import torch
input_size = 5
output_size = 2
input = torch.randn(input_size, output_size)
torch.nn.init.xavier_normal_(input)
print(input)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_uniform_\ntorch.nn.init.xavier_uniform_(tensor, gain=1.0)\n'
import torch
import torch
input_size = 5
output_size = 2
input = torch.randn(input_size, output_size)
torch.nn.init.xavier_uniform_(input)