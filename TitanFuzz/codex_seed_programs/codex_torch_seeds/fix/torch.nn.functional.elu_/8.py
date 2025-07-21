'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu_\ntorch.nn.functional.elu_(input, alpha=1.)\n'
import torch
import torch
input_data = torch.randn(2, 3)
print(input_data)
output_data = torch.nn.functional.elu_(input_data)
print(output_data)