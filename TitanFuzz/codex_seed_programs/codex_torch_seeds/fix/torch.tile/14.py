'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tile\ntorch.tile(input, reps)\n'
import torch
input_data = torch.tensor([[1, 2], [3, 4]])
print(input_data)
print(torch.tile(input_data, (2, 1)))
print(torch.tile(input_data, (1, 2)))
print(torch.tile(input_data, (2, 2)))