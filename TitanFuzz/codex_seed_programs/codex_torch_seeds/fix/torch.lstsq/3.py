'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lstsq\ntorch.lstsq(input, A, *, out=None)\n'
import torch
batch_size = 10
input_size = 3
output_size = 2
input = torch.randn(batch_size, input_size, requires_grad=True)
target = torch.randn(batch_size, output_size)
torch.lstsq(input, target)