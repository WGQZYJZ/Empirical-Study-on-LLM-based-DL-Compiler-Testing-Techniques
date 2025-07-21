'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcmul\ntorch.Tensor.addcmul(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
print('PyTorch version: ', torch.__version__)
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
tensor1 = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
tensor2 = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('input_tensor = ', input_tensor)
print('tensor1 = ', tensor1)
print('tensor2 = ', tensor2)
print('torch.Tensor.addcmul(input_tensor, tensor1, tensor2) = ', torch.Tensor.addcmul(input_tensor, tensor1, tensor2))