'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softsign\ntorch.nn.functional.softsign(input)\n'
import torch
import numpy as np
input_data = torch.tensor([(- 1), 0, 1])
print(torch.nn.functional.softsign(input_data))