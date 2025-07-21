'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.ones_\ntorch.nn.init.ones_(tensor)\n'
import torch
input_tensor = torch.FloatTensor(3, 3)
print('Input Tensor: \n{}'.format(input_tensor))
torch.nn.init.ones_(input_tensor)
print('Output Tensor: \n{}'.format(input_tensor))