'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu\ntorch.nn.functional.elu(input, alpha=1.0, inplace=False)\n'
import torch
import torch
input_data = torch.tensor([(- 1.0), 1.0, 2.0, 3.0, 4.0, 5.0])
output_data = torch.nn.functional.elu(input_data)
print(output_data)