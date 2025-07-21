'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_left_shift_\ntorch.Tensor.bitwise_left_shift_(_input_tensor, other)\n'
import torch
import numpy as np
input_tensor = torch.Tensor(np.array([[1, 2, 3], [4, 5, 6]]))
other = torch.Tensor(np.array([[1, 2, 3], [4, 5, 6]]))
torch.Tensor.bitwise_left_shift_(input_tensor, other)
print(input_tensor)