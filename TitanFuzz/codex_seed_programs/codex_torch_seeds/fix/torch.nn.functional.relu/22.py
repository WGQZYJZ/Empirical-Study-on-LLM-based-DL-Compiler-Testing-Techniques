'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu\ntorch.nn.functional.relu(input, inplace=False)\n'
import torch
input_data = torch.tensor([(- 1.0), 1.0, 3.0], dtype=torch.float)
output = torch.nn.functional.relu(input_data)
print(output)