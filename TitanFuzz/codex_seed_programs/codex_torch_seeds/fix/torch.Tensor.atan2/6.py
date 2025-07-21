'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.atan2\ntorch.Tensor.atan2(_input_tensor, other)\n'
import torch
import numpy as np
import torch
x = np.array([[(- 1), (- 1)], [0, 1], [1, (- 1)]])
x = torch.from_numpy(x)
print(x.atan2(0))