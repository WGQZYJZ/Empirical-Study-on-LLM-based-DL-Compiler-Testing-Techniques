'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.LongStorage\ntorch.LongStorage(*args, **kwargs)\n'
import torch
import numpy as np
input_data = np.random.randn(5, 2)
input_data = torch.from_numpy(input_data)
print('Input data: ', input_data)
input_size = torch.LongStorage(input_data.size())
print('Input size: ', input_size)