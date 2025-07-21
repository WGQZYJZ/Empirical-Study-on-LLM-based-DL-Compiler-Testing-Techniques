'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.positive\ntorch.positive(input)\n'
import torch
input = torch.tensor([(- 1.0), 0.0, 1.0])
output = torch.positive(input)
print(output)