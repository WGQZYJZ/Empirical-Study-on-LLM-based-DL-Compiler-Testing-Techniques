'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addr_\ntorch.Tensor.addr_(_input_tensor, vec1, vec2, *, beta=1, alpha=1)\n'
import torch
import torch
tensor_a = torch.randn(4, 3)
tensor_b = torch.randn(4, 1)
tensor_c = torch.randn(3, 4)
torch.Tensor.addr_(tensor_a, tensor_b, tensor_c)
print(tensor_a)
import torch
tensor_a = torch.randn(4, 3)
tensor_b = torch.randn(4, 1)
tensor_c = torch.randn(3, 4)
torch.Tensor.addr_(tensor_a, tensor_b, tensor_c, beta=0.5, alpha=0.5)
print(tensor_a)