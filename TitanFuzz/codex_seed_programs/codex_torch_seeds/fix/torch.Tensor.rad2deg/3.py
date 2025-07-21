'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rad2deg\ntorch.Tensor.rad2deg(_input_tensor)\n'
import torch
import math
input_tensor = torch.Tensor([0, (math.pi / 2), math.pi])
output_tensor = torch.Tensor.rad2deg(input_tensor)
print('The result is: ', output_tensor)