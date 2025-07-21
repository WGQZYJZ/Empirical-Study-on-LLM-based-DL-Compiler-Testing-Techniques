'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Sequential\ntorch.nn.Sequential(*args)\n'
import torch
input_size = 3
output_size = 2
batch_size = 1
input_data = torch.randn(batch_size, input_size)
model = torch.nn.Sequential(torch.nn.Linear(input_size, output_size), torch.nn.Sigmoid())
output = model(input_data)
print('output: ', output)