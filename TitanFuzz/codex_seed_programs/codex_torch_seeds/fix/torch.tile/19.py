'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tile\ntorch.tile(input, reps)\n'
import torch
input_data = torch.arange(9)
input_data = input_data.reshape(3, 3)
print(input_data)
output_data = torch.tile(input_data, (2, 3))
print(output_data)