'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad3d\ntorch.nn.ConstantPad3d(padding, value)\n'
import torch
import torch
input_data = torch.tensor([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]])
pad_value = torch.tensor(0)
pad_size = (1, 2, 1, 2)
pad_layer = torch.nn.ConstantPad3d(pad_size, pad_value)
output_data = pad_layer(input_data)
print(output_data)