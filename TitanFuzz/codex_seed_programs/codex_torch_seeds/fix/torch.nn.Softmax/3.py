'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax\ntorch.nn.Softmax(dim=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
softmax = torch.nn.Softmax()
output = softmax(input_data)
print(output)