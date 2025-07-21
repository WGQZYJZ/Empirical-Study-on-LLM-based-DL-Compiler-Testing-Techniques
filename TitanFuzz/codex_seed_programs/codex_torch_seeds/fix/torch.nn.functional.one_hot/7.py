'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.one_hot\ntorch.nn.functional.one_hot(tensor, num_classes=-1)\n'
import torch
input = torch.tensor([[0, 1, 2, 3], [1, 2, 3, 4]])
print(input)
output = torch.nn.functional.one_hot(input, num_classes=(- 1))
print(output)
'\nTask 4: Call the API torch.nn.functional.one_hot\ntorch.nn.functional.one_hot(tensor, num_classes=5)\n'
input = torch.tensor([[0, 1, 2, 3], [1, 2, 3, 4]])
print(input)
output = torch.nn.functional.one_hot(input, num_classes=5)
print(output)
'\nTask 5: Call the API torch.nn.functional.one_hot\ntorch.nn.functional.one_hot(tensor, num_classes=5, dtype=torch.float32)\n'
input = torch.tensor([[0, 1, 2, 3], [1, 2, 3, 4]])
print(input)
output = torch.nn.functional