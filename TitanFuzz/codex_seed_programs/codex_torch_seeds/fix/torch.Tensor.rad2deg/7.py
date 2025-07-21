'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rad2deg\ntorch.Tensor.rad2deg(_input_tensor)\n'
import torch
import math
data = torch.randn(3, 3)
print(data)
result = torch.Tensor.rad2deg(data)
print(result)
print(math.degrees(data[0][0]))
print(result[0][0])