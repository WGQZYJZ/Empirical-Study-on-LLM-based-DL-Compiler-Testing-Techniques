'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcmul_\ntorch.Tensor.addcmul_(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
input_data = torch.randn(2, 3)
print('input_data: ', input_data)
tensor1 = torch.randn(2, 3)
print('tensor1: ', tensor1)
tensor2 = torch.randn(2, 3)
print('tensor2: ', tensor2)
input_data.addcmul_(tensor1, tensor2)
print('input_data: ', input_data)