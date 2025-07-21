'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ModuleList\ntorch.nn.ModuleList(modules=None)\n'
import torch
from torch.nn import ModuleList
input_data = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
print('The input data is: ')
print(input_data)
ml = ModuleList([torch.nn.Linear(3, 4), torch.nn.ReLU()])
print('The ModuleList is: ')
print(ml)