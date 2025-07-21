'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.take_along_dim\ntorch.Tensor.take_along_dim(_input_tensor, indices, dim)\n'
import torch
input_tensor = torch.randint(0, 10, (4, 5))
indices = torch.tensor([1, 3])
dim = 0
output_tensor = input_tensor.take_along_dim(indices, dim)
print(output_tensor)