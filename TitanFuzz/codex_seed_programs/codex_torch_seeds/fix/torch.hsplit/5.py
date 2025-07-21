'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hsplit\ntorch.hsplit(input, indices_or_sections)\n'
import torch
tensor_data = torch.arange(0, 20)
print(tensor_data)
tensor_data_split = torch.hsplit(tensor_data, 5)
print(tensor_data_split)
tensor_data_split = torch.hsplit(tensor_data, [3, 4, 6, 10])
print(tensor_data_split)