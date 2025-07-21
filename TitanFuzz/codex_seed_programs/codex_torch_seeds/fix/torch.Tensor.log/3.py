'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log\ntorch.Tensor.log(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
log_tensor = input_tensor.log()
print('input_tensor:', input_tensor)
print('log_tensor:', log_tensor)