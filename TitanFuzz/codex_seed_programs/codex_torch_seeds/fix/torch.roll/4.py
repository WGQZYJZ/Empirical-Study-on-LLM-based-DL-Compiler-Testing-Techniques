'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.roll\ntorch.roll(input, shifts, dims=None)\n'
import torch
data = torch.rand(4, 4)
print('Input data: ', data)
data_rolled = torch.roll(data, shifts=1, dims=1)
print('Data rolled: ', data_rolled)