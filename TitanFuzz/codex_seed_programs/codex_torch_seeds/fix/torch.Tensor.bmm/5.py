'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bmm\ntorch.Tensor.bmm(_input_tensor, batch2)\n'
import torch
import numpy as np
input_tensor = torch.randint(low=0, high=10, size=(3, 2, 4), dtype=torch.float32)
batch2 = torch.randint(low=0, high=10, size=(3, 4, 5), dtype=torch.float32)
output_tensor = torch.Tensor.bmm(input_tensor, batch2)
print(output_tensor)