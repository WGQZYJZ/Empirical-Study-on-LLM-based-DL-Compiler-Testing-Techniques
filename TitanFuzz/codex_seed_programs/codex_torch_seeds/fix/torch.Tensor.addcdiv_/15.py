'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcdiv_\ntorch.Tensor.addcdiv_(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
tensor1 = torch.Tensor([[1, 2, 3], [4, 5, 6]])
tensor2 = torch.Tensor([[1, 2, 3], [4, 5, 6]])
torch.Tensor.addcdiv_(input_tensor, tensor1, tensor2, value=1)
print(input_tensor)