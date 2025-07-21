'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcmul\ntorch.Tensor.addcmul(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
import torch
input_tensor = torch.tensor([[1, 2], [3, 4], [5, 6]], dtype=torch.float32)
tensor1 = torch.tensor([[1, 2], [3, 4], [5, 6]], dtype=torch.float32)
tensor2 = torch.tensor([[1, 2], [3, 4], [5, 6]], dtype=torch.float32)
torch.Tensor.addcmul(input_tensor, tensor1, tensor2, value=1)
print(input_tensor)