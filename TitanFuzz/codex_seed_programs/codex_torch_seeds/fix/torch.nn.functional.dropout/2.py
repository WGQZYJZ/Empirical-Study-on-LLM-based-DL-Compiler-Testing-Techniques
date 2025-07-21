'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.dropout\ntorch.nn.functional.dropout(input, p=0.5, training=True, inplace=False)\n'
import torch
import torch.nn.functional as F
import torch
input_data = torch.randn(10, 20)
output = F.dropout(input_data, p=0.5, training=True)
print(output)
print(output.size())
print(torch.sum(output))
print(torch.equal(output, input_data))
print(torch.sum(output))
print(torch.equal(output, input_data))