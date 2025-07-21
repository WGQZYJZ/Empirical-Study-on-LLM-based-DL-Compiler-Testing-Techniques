'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.logsigmoid\ntorch.nn.functional.logsigmoid(input)\n'
import torch
input_data = torch.tensor([(- 1.0), 0.0, 1.0])
print(torch.nn.functional.logsigmoid(input_data))