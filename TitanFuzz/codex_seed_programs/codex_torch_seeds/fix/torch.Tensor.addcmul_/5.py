'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcmul_\ntorch.Tensor.addcmul_(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
input_tensor = torch.randn(3, 3, requires_grad=True)
tensor1 = torch.randn(3, 3)
tensor2 = torch.randn(3, 3)
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('\nTask 2: Generate input data')
print('input_tensor: ', input_tensor)
print('tensor1: ', tensor1)
print('tensor2: ', tensor2)
print('\nTask 3: Call the API torch.Tensor.addcmul_')
torch.Tensor.addcmul_(input_tensor, tensor1, tensor2, value=1)
print('input_tensor: ', input_tensor)