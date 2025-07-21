'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu_\ntorch.nn.functional.relu_(input)\n'
import torch
input_data = torch.tensor([(- 1), 2, 3, (- 5), (- 8), 0, (- 9), 2], dtype=torch.float)
output = torch.nn.functional.relu_(input_data)
print(output)