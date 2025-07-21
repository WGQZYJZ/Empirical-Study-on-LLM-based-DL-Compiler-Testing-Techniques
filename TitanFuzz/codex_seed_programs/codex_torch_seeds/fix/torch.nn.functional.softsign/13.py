'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softsign\ntorch.nn.functional.softsign(input)\n'
import torch
input_data = torch.tensor([(- 2.0), (- 1.0), 0.0, 1.0, 2.0])
print(torch.nn.functional.softsign(input_data))