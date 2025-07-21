'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.positive\ntorch.positive(input)\n'
import torch
input_data = torch.randn(10, 10)
output_data = torch.positive(input_data)
print(input_data)
print(output_data)