'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.chunk\ntorch.Tensor.chunk(_input_tensor, chunks, dim=0)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
chunked_tensor = input_tensor.chunk(2, dim=0)
print(chunked_tensor)