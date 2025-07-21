'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu_\ntorch.nn.functional.relu_(input)\n'
import torch
input_data = torch.tensor([(- 1), (- 0.5), 0, 0.5, 1], dtype=torch.float32)
print(torch.nn.functional.relu_(input_data))