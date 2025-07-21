'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.numpy\ntorch.Tensor.numpy(_input_tensor)\n'
import torch
input_tensor = torch.ones(3, 3)
print(input_tensor)
output_tensor = input_tensor.numpy()
print(output_tensor)
'\nTask 4: Call the API torch.from_numpy\ntorch.from_numpy(_input_numpy)\n'
import torch
import numpy as np
input_numpy = np.ones((3, 3))
print(input_numpy)
output_tensor = torch.from_numpy(input_numpy)
print(output_tensor)
'\nTask 5: Call the API torch.Tensor.item\ntorch.Tensor.item(_input_tensor)\n'
import torch
input_tensor = torch.ones(1)
print(input_tensor)
output_value = input_tensor.item()
print(output_value)