'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dense_dim\ntorch.Tensor.dense_dim(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
print(input_tensor)
print(torch.Tensor.dense_dim(input_tensor))