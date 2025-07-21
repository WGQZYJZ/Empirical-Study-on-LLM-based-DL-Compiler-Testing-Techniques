'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
import numpy as np
input_data = np.random.rand(3, 3, 3)
input_data = torch.from_numpy(input_data)
print(torch.nn.ConstantPad1d(2, 3)(input_data))