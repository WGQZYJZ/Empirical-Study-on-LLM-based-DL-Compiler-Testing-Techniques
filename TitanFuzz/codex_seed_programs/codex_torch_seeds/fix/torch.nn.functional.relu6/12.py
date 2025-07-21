'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu6\ntorch.nn.functional.relu6(input, inplace=False)\n'
import torch
import numpy as np
input_data = np.array([(- 1), (- 0.5), 0, 0.5, 1])
input_data = torch.Tensor(input_data)
output = torch.nn.functional.relu6(input_data)
print(output)