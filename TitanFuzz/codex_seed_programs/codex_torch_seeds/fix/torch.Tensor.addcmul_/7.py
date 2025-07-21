'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcmul_\ntorch.Tensor.addcmul_(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
input_tensor = torch.randn(3, 3)
tensor1 = torch.randn(3, 3)
tensor2 = torch.randn(3, 3)
print('Input Tensor: \n', input_tensor)
print('Tensor1: \n', tensor1)
print('Tensor2: \n', tensor2)
torch.Tensor.addcmul_(input_tensor, tensor1, tensor2)
print('Output Tensor: \n', input_tensor)
torch.Tensor.addcmul_(input_tensor, tensor1, tensor2, value=2)
print('Output Tensor: \n', input_tensor)