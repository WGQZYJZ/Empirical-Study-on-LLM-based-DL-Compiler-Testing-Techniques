'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.column_stack\ntorch.column_stack(tensors, *, out=None)\n'
import torch
data_1 = torch.rand(4, 4)
data_2 = torch.rand(4, 4)
data_3 = torch.column_stack((data_1, data_2))
print('data_1:', data_1)
print('data_2:', data_2)
print('data_3:', data_3)