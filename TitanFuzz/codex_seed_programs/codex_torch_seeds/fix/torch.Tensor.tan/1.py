'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tan\ntorch.Tensor.tan(_input_tensor)\n'
import torch
import numpy as np
input_tensor = torch.Tensor(np.random.rand(3, 3))
output_tensor = torch.Tensor.tan(input_tensor)
print(input_tensor)
print(output_tensor)