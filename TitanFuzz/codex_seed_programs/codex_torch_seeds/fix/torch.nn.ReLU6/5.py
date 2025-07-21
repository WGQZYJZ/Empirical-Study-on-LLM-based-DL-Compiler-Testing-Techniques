'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU6\ntorch.nn.ReLU6(inplace=False)\n'
import torch
input_data = torch.tensor([(- 1), (- 0.5), 0, 0.5, 1])
output_data = torch.nn.ReLU6(inplace=False)(input_data)
print('Input data:\n{}'.format(input_data))
print('Output data:\n{}'.format(output_data))
output_data = torch.nn.ReLU6(inplace=True)(input_data)
print('Input data:\n{}'.format(input_data))
print('Output data:\n{}'.format(output_data))