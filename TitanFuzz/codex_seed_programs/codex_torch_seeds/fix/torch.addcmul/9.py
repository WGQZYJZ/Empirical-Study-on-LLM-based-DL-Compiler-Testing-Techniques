'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcmul\ntorch.addcmul(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
tensor_a = torch.tensor([1, 2, 3], dtype=torch.float32)
tensor_b = torch.tensor([4, 5, 6], dtype=torch.float32)
tensor_c = torch.tensor([7, 8, 9], dtype=torch.float32)
print(torch.addcmul(tensor_a, tensor_b, tensor_c))
print(torch.addcmul(tensor_a, tensor_b, tensor_c, value=2))
print(torch.addcmul(tensor_a, tensor_b, tensor_c, value=2, out=tensor_a))
print(tensor_a)