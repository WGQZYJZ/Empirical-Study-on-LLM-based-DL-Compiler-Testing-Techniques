'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ravel\ntorch.ravel(input)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input_data)
print(torch.ravel(input_data))
print(torch.flatten(input_data))
print(torch.reshape(input_data, (6,)))
print(torch.squeeze(input_data))
print(torch.unsqueeze(input_data, 0))
print(torch.transpose(input_data, 0, 1))