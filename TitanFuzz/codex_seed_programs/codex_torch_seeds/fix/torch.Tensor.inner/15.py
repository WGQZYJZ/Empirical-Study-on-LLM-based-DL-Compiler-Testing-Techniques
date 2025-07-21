'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.inner\ntorch.Tensor.inner(_input_tensor, other)\n'
import torch
from typing import Tuple
from typing import List
input_tensor1 = torch.tensor([1, 2, 3, 4, 5])
input_tensor2 = torch.tensor([5, 4, 3, 2, 1])
result = torch.Tensor.inner(input_tensor1, input_tensor2)
print(result)