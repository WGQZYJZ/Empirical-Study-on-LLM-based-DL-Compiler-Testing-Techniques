'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.one_hot\ntorch.nn.functional.one_hot(tensor, num_classes=-1)\n'
import torch
input_data = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print('Input data: {}'.format(input_data))
output_data = torch.nn.functional.one_hot(input_data, num_classes=3)
print('Output data: {}'.format(output_data))