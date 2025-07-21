'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcmul\ntorch.addcmul(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
tensor_1 = torch.randn(3, 3)
tensor_2 = torch.randn(3, 3)
tensor_3 = torch.randn(3, 3)
print(tensor_1)
print(tensor_2)
print(tensor_3)
tensor_4 = torch.addcmul(tensor_1, tensor_2, tensor_3)
print(tensor_4)