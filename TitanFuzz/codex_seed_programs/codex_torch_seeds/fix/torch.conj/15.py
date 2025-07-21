'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.conj\ntorch.conj(input)\n'
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
print('Input tensor:\n', input_tensor)
output_tensor = torch.conj(input_tensor)
print('Output tensor:\n', output_tensor)