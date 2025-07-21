'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.acosh_\ntorch.Tensor.acosh_(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, dtype=torch.float32)
print('\nInput tensor: ', input_tensor)
acosh_output = input_tensor.acosh_()
print('\nOutput tensor: ', acosh_output)