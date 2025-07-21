'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.put_\ntorch.Tensor.put_(_input_tensor, index, source, accumulate=False)\n'
import torch
input_tensor = torch.randint(0, 10, (3, 3))
print('Input tensor: {}'.format(input_tensor))
index = torch.tensor([[0, 1], [1, 2]])
source = torch.tensor([11, 12])
input_tensor.put_(index, source)
print('Output tensor: {}'.format(input_tensor))