'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reshape\ntorch.reshape(input, shape)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(input_tensor)
output_tensor = torch.reshape(input_tensor, (2, 6))
print(output_tensor)
output_tensor = torch.reshape(input_tensor, (1, 12))
print(output_tensor)
output_tensor = torch.reshape(input_tensor, (12, 1))
print(output_tensor)