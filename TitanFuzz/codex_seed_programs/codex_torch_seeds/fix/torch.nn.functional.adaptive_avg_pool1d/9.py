'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool1d\ntorch.nn.functional.adaptive_avg_pool1d(input, output_size)\n'
import torch
import numpy as np
input_data = torch.tensor(np.random.random((1, 1, 10)), dtype=torch.float32)
output_data = torch.nn.functional.adaptive_avg_pool1d(input_data, 2)
print(output_data)