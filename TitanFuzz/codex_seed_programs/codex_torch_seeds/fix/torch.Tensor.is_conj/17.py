'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_conj\ntorch.Tensor.is_conj(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print(input_tensor.is_conj())
input_tensor = torch.tensor([[(1 + 2j), (2 + 3j), (3 + 4j)], [(4 + 5j), (5 + 6j), (6 + 7j)]])
print(input_tensor.is_conj())