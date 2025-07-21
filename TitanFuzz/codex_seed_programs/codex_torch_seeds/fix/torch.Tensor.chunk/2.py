'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.chunk\ntorch.Tensor.chunk(_input_tensor, chunks, dim=0)\n'
import torch
input_tensor = torch.randn(4, 4)
chunks = 2
dim = 0
print(input_tensor.chunk(chunks, dim))