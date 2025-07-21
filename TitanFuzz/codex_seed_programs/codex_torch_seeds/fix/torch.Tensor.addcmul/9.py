'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcmul\ntorch.Tensor.addcmul(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
input_tensor = torch.randn(5, 5, dtype=torch.float)
tensor1 = torch.randn(5, 5, dtype=torch.float)
tensor2 = torch.randn(5, 5, dtype=torch.float)
torch.Tensor.addcmul(input_tensor, tensor1, tensor2)