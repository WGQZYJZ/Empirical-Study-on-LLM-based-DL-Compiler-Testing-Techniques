'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.scatter\ntorch.Tensor.scatter(_input_tensor, dim, index, src)\n'
import torch
input_tensor = torch.rand(4, 4)
index_tensor = torch.tensor([[0, 2, 2, 0], [0, 0, 1, 1]])
src_tensor = torch.tensor([3.1415, 2.7182])
output_tensor = input_tensor.scatter(0, index_tensor, src_tensor)
print(output_tensor)