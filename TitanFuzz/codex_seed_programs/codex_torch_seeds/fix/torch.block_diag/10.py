'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.block_diag\ntorch.block_diag(*tensors)\n'
import torch
input_data = [[1, 2, 3], [4, 5, 6]]
input_data = torch.tensor(input_data)
output = torch.block_diag(input_data)
print('output is: ', output)