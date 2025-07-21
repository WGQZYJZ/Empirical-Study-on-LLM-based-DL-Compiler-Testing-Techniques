'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.one_hot\ntorch.nn.functional.one_hot(tensor, num_classes=-1)\n'
import torch
from torch import nn
input_tensor = torch.tensor([[0, 1, 2, 3]])
output_tensor = nn.functional.one_hot(input_tensor, num_classes=4)
print(output_tensor)