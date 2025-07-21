'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSigmoid\ntorch.nn.LogSigmoid()\n'
import torch
input_data = torch.tensor([[1.0, (- 1.0), 0.0], [0.0, 0.0, 0.0]])
output = torch.nn.LogSigmoid()(input_data)
print('input_data:', input_data)
print('output:', output)