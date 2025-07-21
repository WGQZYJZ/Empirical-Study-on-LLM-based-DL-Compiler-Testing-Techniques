"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pad\ntorch.nn.functional.pad(input, pad, mode='constant', value=0)\n"
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input_data)
padded_data = torch.nn.functional.pad(input_data, (1, 1, 2, 2), mode='constant', value=0)
print(padded_data)