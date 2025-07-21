'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sign\ntorch.Tensor.sign(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3)
print('input_tensor: ', input_tensor)
sign_tensor = input_tensor.sign()
print('sign_tensor: ', sign_tensor)