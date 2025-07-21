'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcmul\ntorch.addcmul(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
data1 = torch.rand(2, 3, 4)
data2 = torch.rand(2, 3, 4)
data3 = torch.rand(2, 3, 4)
result = torch.addcmul(data1, data2, data3, value=0.5)
print(result)