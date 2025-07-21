'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad3d\ntorch.nn.ConstantPad3d(padding, value)\n'
import torch
import torch
input_data = torch.randint(1, 5, (2, 3, 4, 5), dtype=torch.float32)
print(input_data)
pad_size = (1, 2, 3, 4)
value = 0.0
pad3d = torch.nn.ConstantPad3d(pad_size, value)
output = pad3d(input_data)
print(output)