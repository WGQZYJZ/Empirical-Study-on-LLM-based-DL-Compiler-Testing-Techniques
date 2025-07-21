'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_zero_point\ntorch.Tensor.q_zero_point(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 3)
print('Input tensor: ', input_tensor)
zero_point = input_tensor.q_zero_point()
print('Zero point: ', zero_point)