'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addr\ntorch.Tensor.addr(_input_tensor, vec1, vec2, *, beta=1, alpha=1)\n'
import torch
input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
vec1 = torch.tensor([7.0, 8.0, 9.0])
vec2 = torch.tensor([10.0, 11.0, 12.0])
output_tensor = torch.Tensor.addr(input_tensor, vec1, vec2)
print(output_tensor)