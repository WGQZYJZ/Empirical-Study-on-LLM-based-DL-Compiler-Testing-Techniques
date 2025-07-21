'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
input = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
pad_size = 1
value = 0
padded_input = torch.nn.ConstantPad1d(pad_size, value)(input)
print(padded_input)