'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSigmoid\ntorch.nn.LogSigmoid()\n'
import torch
data = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=torch.float)
output = torch.nn.LogSigmoid()
print(output(data))