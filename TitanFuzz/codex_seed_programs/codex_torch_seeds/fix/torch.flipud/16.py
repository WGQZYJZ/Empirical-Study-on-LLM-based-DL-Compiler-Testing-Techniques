'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flipud\ntorch.flipud(input)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input_data)
output_data = torch.flipud(input_data)
print(output_data)