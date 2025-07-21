'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.multi_dot\ntorch.linalg.multi_dot(tensors, *, out=None)\n'
import torch
input_data1 = torch.randn(3, 3)
input_data2 = torch.randn(3, 3)
input_data3 = torch.randn(3, 3)
result = torch.linalg.multi_dot([input_data1, input_data2, input_data3])
print(result)