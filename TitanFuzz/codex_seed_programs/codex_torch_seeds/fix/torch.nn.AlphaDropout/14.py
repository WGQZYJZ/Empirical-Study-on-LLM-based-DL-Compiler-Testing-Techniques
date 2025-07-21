'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AlphaDropout\ntorch.nn.AlphaDropout(p=0.5, inplace=False)\n'
import torch
input_data = torch.randn(3, 3, requires_grad=True)
print('Input data: \n{}'.format(input_data))
dropout = torch.nn.AlphaDropout(p=0.5, inplace=False)
output = dropout(input_data)
print('Output data: \n{}'.format(output))