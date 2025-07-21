'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tile\ntorch.tile(input, reps)\n'
import torch
input_data = torch.arange(1, 17, dtype=torch.float32).reshape(4, 4)
print('Input data:\n', input_data)
reps = (2, 1)
output = torch.tile(input_data, reps)
print('Output data:\n', output)