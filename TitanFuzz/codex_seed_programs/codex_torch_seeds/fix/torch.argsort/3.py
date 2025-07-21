'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argsort\ntorch.argsort(input, dim=-1, descending=False)\n'
import torch
input_data = torch.randint(0, 10, (4, 4))
print('Input data:\n', input_data)
sort_indices = torch.argsort(input_data, dim=(- 1), descending=False)
print('Sort indices:\n', sort_indices)
sorted_data = torch.sort(input_data, dim=(- 1), descending=False)
print('Sorted data:\n', sorted_data)
(top3_data, top3_indices) = torch.topk(input_data, 3, dim=(- 1), largest=True)
print('Top3 data:\n', top3_data)
print('Top3 indices:\n', top3_indices)