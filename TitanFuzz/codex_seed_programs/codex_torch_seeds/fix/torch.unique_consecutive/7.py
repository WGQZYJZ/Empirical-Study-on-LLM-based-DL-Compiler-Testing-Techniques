'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unique_consecutive\ntorch.unique_consecutive(input, return_inverse=False, return_counts=False, dim=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 3, 3, 3, 3, 4], [1, 2, 3, 4, 4, 4, 4, 4]])
output_data = torch.unique_consecutive(input_data, return_inverse=True, return_counts=True)
print(output_data)