'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.one_hot\ntorch.nn.functional.one_hot(tensor, num_classes=-1)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
output_data = torch.nn.functional.one_hot(input_data)
print(output_data)