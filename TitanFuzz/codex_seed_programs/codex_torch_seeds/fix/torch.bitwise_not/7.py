'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_not\ntorch.bitwise_not(input, *, out=None)\n'
import torch
input_tensor = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print('Input tensor: ', input_tensor)
inverted_tensor = torch.bitwise_not(input_tensor)
print('Inverted tensor: ', inverted_tensor)