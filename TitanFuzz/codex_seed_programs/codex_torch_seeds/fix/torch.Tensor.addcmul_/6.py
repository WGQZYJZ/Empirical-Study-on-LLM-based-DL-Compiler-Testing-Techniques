'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcmul_\ntorch.Tensor.addcmul_(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
tensor1 = torch.rand(4, 4)
tensor2 = torch.rand(4, 4)
tensor3 = torch.rand(4, 4)
tensor3.addcmul_(tensor1, tensor2)
print(tensor3)
print(tensor1)
print(tensor2)