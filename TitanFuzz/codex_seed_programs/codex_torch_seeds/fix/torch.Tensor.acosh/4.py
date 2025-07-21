'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.acosh\ntorch.Tensor.acosh(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 4, 5)
acosh_tensor = input_tensor.acosh()
print('input_tensor =', input_tensor)
print('acosh_tensor =', acosh_tensor)