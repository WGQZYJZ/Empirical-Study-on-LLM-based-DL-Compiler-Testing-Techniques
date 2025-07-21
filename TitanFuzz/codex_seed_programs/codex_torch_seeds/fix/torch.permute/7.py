'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.permute\ntorch.permute(input, dims)\n'
import torch
input_data = torch.tensor([[1, 2], [3, 4]])
print(input_data)
output_data = torch.permute(input_data, (1, 0))
print(output_data)