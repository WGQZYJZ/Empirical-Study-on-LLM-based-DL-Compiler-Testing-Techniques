'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.acosh_\ntorch.Tensor.acosh_(_input_tensor)\n'
import torch
_input_tensor = torch.rand(1, 3, 4, 5)
acosh_output = torch.Tensor.acosh_(_input_tensor)
print(acosh_output)