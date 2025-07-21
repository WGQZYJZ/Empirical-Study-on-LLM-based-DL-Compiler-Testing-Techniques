'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.outer\ntorch.Tensor.outer(_input_tensor, vec2)\n'
import torch
import numpy as np
vec1 = torch.tensor(np.random.rand(10), dtype=torch.float32)
vec2 = torch.tensor(np.random.rand(10), dtype=torch.float32)
out = torch.Tensor.outer(vec1, vec2)
print(out)