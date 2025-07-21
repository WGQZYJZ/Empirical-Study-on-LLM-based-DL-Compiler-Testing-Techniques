'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.tanh\ntorch.nn.functional.tanh(input)\n'
import torch
import numpy as np
input_data = np.random.uniform(0, 1, (10, 5))
input_data = torch.from_numpy(input_data)
output_data = torch.nn.functional.tanh(input_data)
print(output_data)