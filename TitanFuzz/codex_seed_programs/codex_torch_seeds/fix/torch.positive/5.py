'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.positive\ntorch.positive(input)\n'
import torch
input_data = torch.rand(1, 5)
print(input_data)
output_data = torch.positive(input_data)
print(output_data)