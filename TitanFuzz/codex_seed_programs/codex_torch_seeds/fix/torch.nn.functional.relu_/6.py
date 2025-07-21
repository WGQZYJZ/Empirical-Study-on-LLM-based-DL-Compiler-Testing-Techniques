'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu_\ntorch.nn.functional.relu_(input)\n'
import torch
input_data = torch.arange((- 5), 5, 0.1)
output_data = torch.nn.functional.relu_(input_data)
print(input_data)
print(output_data)