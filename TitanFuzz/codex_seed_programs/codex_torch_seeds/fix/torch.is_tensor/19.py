'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_tensor\ntorch.is_tensor(obj)\n'
import torch
input_data = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
input_tensor = torch.tensor(input_data)
output = torch.is_tensor(input_tensor)
print(input_tensor)
print(output)