'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcmul_\ntorch.Tensor.addcmul_(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
import torch
input_tensor = torch.randn(2, 3, 4)
tensor1 = torch.randn(2, 3, 4)
tensor2 = torch.randn(2, 3, 4)
torch.Tensor.addcmul_(input_tensor, tensor1, tensor2, value=2)
print(input_tensor)