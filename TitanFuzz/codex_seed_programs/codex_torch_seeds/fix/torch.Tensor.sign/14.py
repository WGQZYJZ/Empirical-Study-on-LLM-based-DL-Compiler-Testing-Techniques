'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sign\ntorch.Tensor.sign(_input_tensor)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
print('input tensor:', input_tensor)
sign_tensor = input_tensor.sign()
print('sign tensor:', sign_tensor)
input_tensor.sign_()
print('input tensor after sign_:', input_tensor)