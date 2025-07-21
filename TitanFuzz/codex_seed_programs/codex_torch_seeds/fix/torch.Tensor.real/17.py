'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.real\ntorch.Tensor.real(_input_tensor, )\n'
import torch
input_data = [[1, 2, 3], [4, 5, 6]]
input_tensor = torch.Tensor(input_data)
print('input_tensor:', input_tensor)
real_input_tensor = input_tensor.real()
print('real_input_tensor:', real_input_tensor)