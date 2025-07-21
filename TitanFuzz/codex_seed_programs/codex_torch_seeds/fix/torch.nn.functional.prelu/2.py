'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.prelu\ntorch.nn.functional.prelu(input, weight)\n'
import torch
import torch
input_data = torch.randn(1, 3, 4, 4)
output_data = torch.nn.functional.prelu(input_data, torch.ones(1))
print(output_data)