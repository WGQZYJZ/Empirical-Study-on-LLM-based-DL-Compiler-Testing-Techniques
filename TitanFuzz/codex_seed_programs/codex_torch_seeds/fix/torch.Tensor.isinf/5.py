'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isinf\ntorch.Tensor.isinf(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(input_tensor.isinf())
'\nOutput:\ntensor([[False, False, False],\n        [False, False, False],\n        [False, False, False]])\n'