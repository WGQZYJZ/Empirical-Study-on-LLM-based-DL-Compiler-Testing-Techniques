'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.atan\ntorch.Tensor.atan(_input_tensor)\n'
import torch
input_tensor = torch.tensor([(- 1), 0, 1])
output_tensor = torch.Tensor.atan(input_tensor)
print('Input Tensor:\n', input_tensor)
print('Output Tensor:\n', output_tensor)