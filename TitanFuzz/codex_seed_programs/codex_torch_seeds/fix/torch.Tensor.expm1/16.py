'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.expm1\ntorch.Tensor.expm1(_input_tensor)\n'
import torch
import numpy as np
input_data = np.random.rand(10, 10)
input_tensor = torch.tensor(input_data)
output_tensor = torch.Tensor.expm1(input_tensor)
print(output_tensor)
'\nTask 4: Call the API torch.expm1\ntorch.expm1(_input_tensor)\n'
output_tensor = torch.expm1(input_tensor)
print(output_tensor)