'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.detach\ntorch.Tensor.detach(_input_tensor, )\n'
import torch
import numpy as np
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(data)
tensor = torch.from_numpy(data)
print(tensor)
tensor_detach = tensor.detach()
print(tensor_detach)