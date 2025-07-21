'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reshape\ntorch.reshape(input, shape)\n'
import torch
input_data = torch.randn(2, 3, 4)
output = torch.reshape(input_data, ((- 1), 6))
print(output)