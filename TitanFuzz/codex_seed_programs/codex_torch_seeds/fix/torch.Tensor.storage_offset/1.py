'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.storage_offset\ntorch.Tensor.storage_offset(_input_tensor)\n'
import torch
print(torch.__version__)
input_data = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
input_tensor = torch.tensor(input_data)
print(input_tensor)
print(input_tensor.storage_offset())