'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU\ntorch.nn.ReLU(inplace=False)\n'
import torch
input_data = torch.tensor([(- 1.0), 1.0, 2.0])
print('Input data: ', input_data)
relu = torch.nn.ReLU()
output = relu(input_data)
print('Output: ', output)
relu = torch.nn.ReLU(inplace=True)
output = relu(input_data)
print('Output: ', output)