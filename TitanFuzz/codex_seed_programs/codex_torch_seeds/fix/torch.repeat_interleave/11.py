'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.repeat_interleave\ntorch.repeat_interleave(input, repeats, dim=None)\n'
import torch
input_data = torch.arange(6).view(2, 3)
print(input_data)
output_data = torch.repeat_interleave(input_data, repeats=2, dim=0)
print(output_data)
output_data = torch.repeat_interleave(input_data, repeats=2, dim=1)
print(output_data)
output_data = torch.repeat_interleave(input_data, repeats=2)
print(output_data)