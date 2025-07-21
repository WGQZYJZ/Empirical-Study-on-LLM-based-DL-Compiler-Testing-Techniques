'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad2d\ntorch.nn.ConstantPad2d(padding, value)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
padding = torch.nn.ConstantPad2d((1, 1, 1, 1), 0)
output = padding(input_data)
print(output)