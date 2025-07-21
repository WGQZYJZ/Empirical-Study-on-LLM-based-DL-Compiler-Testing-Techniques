'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.baddbmm\ntorch.Tensor.baddbmm(_input_tensor, batch1, batch2, *, beta=1, alpha=1)\n'
import torch
import numpy as np
batch_size = 2
input_size = 3
hidden_size = 4
input_data = np.random.rand(batch_size, input_size, hidden_size)
batch1 = np.random.rand(batch_size, input_size, hidden_size)
batch2 = np.random.rand(batch_size, input_size, hidden_size)
input_tensor = torch.tensor(input_data, dtype=torch.float32)
tensor1 = torch.tensor(batch1, dtype=torch.float32)
tensor2 = torch.tensor(batch2, dtype=torch.float32)
result = torch.Tensor.baddbmm(input_tensor, tensor1, tensor2, beta=1, alpha=1)
print(result)