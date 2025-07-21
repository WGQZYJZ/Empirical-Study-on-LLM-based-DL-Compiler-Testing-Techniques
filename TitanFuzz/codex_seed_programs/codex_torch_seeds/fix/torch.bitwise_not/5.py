'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_not\ntorch.bitwise_not(input, *, out=None)\n'
import torch
input_data = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.int32)
print('Input data:\n{}'.format(input_data))
output = torch.bitwise_not(input_data)
print('Output:\n{}'.format(output))