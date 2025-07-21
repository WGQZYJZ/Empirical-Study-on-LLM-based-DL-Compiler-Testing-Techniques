'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ConstantPad1d\ntorch.nn.ConstantPad1d(padding, value)\n'
import torch
import torch
input_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=torch.float32)
pad1d = torch.nn.ConstantPad1d((1, 1), 0)
output = pad1d(input_data)
print('Input data:')
print(input_data)
print('Output:')
print(output)