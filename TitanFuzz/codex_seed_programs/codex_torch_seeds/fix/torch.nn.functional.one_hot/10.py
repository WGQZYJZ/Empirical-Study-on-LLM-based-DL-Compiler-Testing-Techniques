'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.one_hot\ntorch.nn.functional.one_hot(tensor, num_classes=-1)\n'
import torch
import torch
input_data = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
output_data = torch.nn.functional.one_hot(input_data, num_classes=10)
print(output_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.embedding\ntorch.nn.functional.embedding(input, weight, padding_idx=-1, scale_grad_by_freq=False, sparse=False)\n'
import torch
import torch
input_data = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])