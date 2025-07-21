'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.chunk\ntorch.Tensor.chunk(_input_tensor, chunks, dim=0)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(5, 4), dtype=torch.int32)
print('Input data:', input_tensor)
output_tensor = input_tensor.chunk(chunks=2, dim=0)
print('Output data:', output_tensor)