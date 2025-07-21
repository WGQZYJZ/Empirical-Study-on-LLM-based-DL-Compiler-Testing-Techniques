'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.one_hot\ntorch.nn.functional.one_hot(tensor, num_classes=-1)\n'
import torch
input = torch.tensor([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]])
output = torch.nn.functional.one_hot(input, num_classes=10)
print(output)