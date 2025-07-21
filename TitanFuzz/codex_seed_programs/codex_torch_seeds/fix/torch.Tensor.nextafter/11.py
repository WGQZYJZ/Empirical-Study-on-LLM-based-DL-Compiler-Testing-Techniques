'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nextafter\ntorch.Tensor.nextafter(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
other = torch.tensor([2.0])
print('Input tensor: {}'.format(input_tensor))
print('Other tensor: {}'.format(other))
print('Result tensor: {}'.format(input_tensor.nextafter(other)))