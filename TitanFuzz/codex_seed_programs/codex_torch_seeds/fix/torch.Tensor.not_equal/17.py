'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.not_equal\ntorch.Tensor.not_equal(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(3, 3))
print('Input Tensor:', input_tensor)
output_tensor = input_tensor.not_equal(0)
print('Output Tensor:', output_tensor)