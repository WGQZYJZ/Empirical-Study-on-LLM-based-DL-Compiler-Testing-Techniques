'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.heaviside\ntorch.Tensor.heaviside(_input_tensor, values)\n'
import torch
input_tensor = torch.randn(3, 3)
step_function = torch.Tensor.heaviside(input_tensor, torch.tensor(0.5))
print('Input Tensor:\n', input_tensor)
print('Step Function:\n', step_function)