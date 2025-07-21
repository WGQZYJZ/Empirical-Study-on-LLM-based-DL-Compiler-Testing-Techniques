'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcmul\ntorch.Tensor.addcmul(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
tensor1 = torch.rand(3, 3)
tensor2 = torch.rand(3, 3)
tensor3 = torch.rand(3, 3)
result = tensor3.addcmul(tensor1, tensor2)
print(result)