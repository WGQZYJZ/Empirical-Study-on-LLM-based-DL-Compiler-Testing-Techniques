'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ravel\ntorch.ravel(input)\n'
import torch
import numpy as np
input_data = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
input_data = torch.from_numpy(input_data)
print(torch.ravel(input_data))