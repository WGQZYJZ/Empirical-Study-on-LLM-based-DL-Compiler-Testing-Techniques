'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.reshape\ntorch.reshape(input, shape)\n'
import torch
'\nTask 1: Generate input data\n'
input_data = torch.randn(2, 3)
print(input_data)
'\nTask 2: Call the API torch.reshape\ntorch.reshape(input, shape)\n'
output_data = torch.reshape(input_data, ((- 1), 3))
print(output_data)
output_data = torch.reshape(input_data, (3, (- 1)))
print(output_data)
output_data = torch.reshape(input_data, (1, 6))
print(output_data)
output_data = torch.reshape(input_data, (6, 1))
print(output_data)
output_data = torch.reshape(input_data, (6,))
print(output_data)
'\nTask 3: Call the API torch.view\ntorch.view(input, shape)\n'
output_data = input_data.view((- 1), 3)
print(output_data)
output_data = input