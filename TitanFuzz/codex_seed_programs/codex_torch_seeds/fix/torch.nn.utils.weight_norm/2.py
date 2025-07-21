"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.weight_norm\ntorch.nn.utils.weight_norm(module, name='weight', dim=0)\n"
import torch
input_data = torch.randn(2, 3, 4)
module = torch.nn.Linear(4, 3)
weight_norm = torch.nn.utils.weight_norm(module)
output = weight_norm(input_data)
print(output)