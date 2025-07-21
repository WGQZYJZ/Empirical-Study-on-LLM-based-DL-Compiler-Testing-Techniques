'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softsign\ntorch.nn.functional.softsign(input)\n'
import torch
import numpy as np
input_data = np.random.randn(2, 3)
input_data = torch.tensor(input_data, dtype=torch.float)
print(input_data)
output_data = torch.nn.functional.softsign(input_data)
print(output_data)