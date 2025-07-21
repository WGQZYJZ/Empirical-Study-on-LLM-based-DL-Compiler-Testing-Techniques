'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcdiv_\ntorch.Tensor.addcdiv_(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
import torch
tensor1 = torch.rand(2, 3, dtype=torch.float32)
tensor2 = torch.rand(2, 3, dtype=torch.float32)
tensor3 = torch.rand(2, 3, dtype=torch.float32)
torch.Tensor.addcdiv_(tensor1, tensor2, tensor3, value=1)
print('tensor1 = ', tensor1)
print('tensor2 = ', tensor2)
print('tensor3 = ', tensor3)