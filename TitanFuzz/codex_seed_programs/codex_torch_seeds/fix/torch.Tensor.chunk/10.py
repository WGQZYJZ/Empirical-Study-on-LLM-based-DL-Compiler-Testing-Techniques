'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.chunk\ntorch.Tensor.chunk(_input_tensor, chunks, dim=0)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
chunk_tensor = input_tensor.chunk(2, dim=1)
print(chunk_tensor)