'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReLU\ntorch.nn.ReLU(inplace=False)\n'
import torch
input_data = torch.tensor([(- 1.0), 1.0, 2.0])
relu = torch.nn.ReLU()
output = relu(input_data)
print(output)