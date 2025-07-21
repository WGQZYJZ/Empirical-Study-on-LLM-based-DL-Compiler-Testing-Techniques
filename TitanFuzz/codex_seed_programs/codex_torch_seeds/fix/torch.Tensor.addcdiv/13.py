'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcdiv\ntorch.Tensor.addcdiv(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
tensor1 = torch.rand(3, 3)
tensor2 = torch.rand(3, 3)
tensor3 = torch.rand(3, 3)
torch.Tensor.addcdiv(tensor1, tensor2, tensor3, value=1)
tensor1.addcdiv(tensor2, tensor3, value=1)