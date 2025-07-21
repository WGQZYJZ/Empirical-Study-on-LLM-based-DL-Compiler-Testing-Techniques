'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU6\ntorch.nn.ReLU6(inplace=False)\n'
import torch
input_data = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0], dtype=torch.float)
relu6 = torch.nn.ReLU6()
output = relu6(input_data)
print('input data is:')
print(input_data)
print('output is:')
print(output)