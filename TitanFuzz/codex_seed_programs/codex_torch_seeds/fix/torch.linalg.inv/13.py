'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.inv\ntorch.linalg.inv(A, *, out=None)\n'
import torch
batch_size = 3
input_size = 3
output_size = 3
input_data = torch.randn(batch_size, input_size, requires_grad=True)
output_data = torch.linalg.inv(input_data)
print(output_data)