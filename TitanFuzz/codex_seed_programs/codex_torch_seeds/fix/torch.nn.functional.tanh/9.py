'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.tanh\ntorch.nn.functional.tanh(input)\n'
import torch
input_data = torch.randn(2, 3)
output = torch.nn.functional.tanh(input_data)
print(input_data)
print(output)