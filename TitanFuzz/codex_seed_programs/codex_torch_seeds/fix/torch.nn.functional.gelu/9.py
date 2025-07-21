'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gelu\ntorch.nn.functional.gelu(input)\n'
import torch
input_data = torch.tensor([[(- 1.0), 0.0, 1.0]])
output_data = torch.nn.functional.gelu(input_data)
print(output_data)
'\nTask 4: Call the API torch.nn.GELU\ntorch.nn.GELU(input)\n'
input_data = torch.tensor([[(- 1.0), 0.0, 1.0]])
output_data = torch.nn.GELU(input_data)
print(output_data)