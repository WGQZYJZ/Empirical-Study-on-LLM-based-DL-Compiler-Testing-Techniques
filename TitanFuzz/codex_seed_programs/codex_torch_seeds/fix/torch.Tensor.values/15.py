'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.values\ntorch.Tensor.values(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.Tensor(np.array([[1, 2, 3], [4, 5, 6]]))
print(torch.Tensor.values(_input_tensor))