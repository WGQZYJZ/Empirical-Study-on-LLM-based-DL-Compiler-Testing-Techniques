'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.add\ntorch.add(input, other, *, alpha=1, out=None)\n'
import torch
print('PyTorch version: ', torch.__version__)
data_1 = torch.Tensor(2, 3)
data_2 = torch.Tensor(2, 3)
data_3 = torch.add(data_1, data_2)
print('data_3: ', data_3)
data_4 = torch.add(data_1, data_2, out=data_3)
print('data_4: ', data_4)
data_5 = torch.add(data_1, data_2, alpha=2)
print('data_5: ', data_5)
data_6 = torch.add(data_1, data_2, alpha=2, out=data_5)