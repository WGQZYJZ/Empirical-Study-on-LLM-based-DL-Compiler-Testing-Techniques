'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sgn\ntorch.Tensor.sgn(_input_tensor)\n'
import torch
import numpy as np
input_data = np.array([[(- 1), (- 2), (- 3)], [4, 5, 6]])
input_tensor = torch.Tensor(input_data)
output_tensor = input_tensor.sgn()
print(output_tensor)