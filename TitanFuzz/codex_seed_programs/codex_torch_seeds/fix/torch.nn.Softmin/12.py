'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmin\ntorch.nn.Softmin(dim=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
print(('-' * 30))
softmin_output = torch.nn.Softmin(dim=1)
print(softmin_output(input_data))
print(('-' * 30))
softmin_output = torch.nn.Softmin(dim=0)
print(softmin_output(input_data))
print(('-' * 30))
softmin_output = torch.nn.Softmin()
print(softmin_output(input_data))
print(('-' * 30))