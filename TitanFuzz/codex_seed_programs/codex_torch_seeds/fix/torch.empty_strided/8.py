'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.empty_strided\ntorch.empty_strided(size, stride, *, dtype=None, layout=None, device=None, requires_grad=False, pin_memory=False)\n'
import torch
import numpy as np
np_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
tensor = torch.from_numpy(np_array)
tensor_strided = torch.empty_strided(tensor.size(), tensor.stride())
print(tensor)
print(tensor_strided)