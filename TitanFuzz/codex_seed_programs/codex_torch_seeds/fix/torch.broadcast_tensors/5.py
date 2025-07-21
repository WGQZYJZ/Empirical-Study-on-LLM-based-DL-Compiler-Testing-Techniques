'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_tensors\ntorch.broadcast_tensors(*tensors)\n'
import torch
input_data = torch.randn(2, 3)
output_data = torch.broadcast_tensors(input_data, input_data)
print(output_data)