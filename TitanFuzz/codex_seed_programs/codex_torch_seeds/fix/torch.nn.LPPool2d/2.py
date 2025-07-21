'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LPPool2d\ntorch.nn.LPPool2d(norm_type, kernel_size, stride=None, ceil_mode=False)\n'
import torch
import torch
input_data = torch.arange(1, 17, dtype=torch.float32).view(1, 1, 4, 4)
pool = torch.nn.LPPool2d(2, 3, stride=2)
output = pool(input_data)
print('The input size is: {}'.format(input_data.size()))
print('The output size is: {}'.format(output.size()))
print('The output data is: \n{}'.format(output))