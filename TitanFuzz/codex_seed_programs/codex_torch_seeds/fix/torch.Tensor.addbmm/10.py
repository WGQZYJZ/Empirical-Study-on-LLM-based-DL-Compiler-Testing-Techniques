'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addbmm\ntorch.Tensor.addbmm(_input_tensor, batch1, batch2, *, beta=1, alpha=1)\n'
import torch
batch_size = 3
input_size = 5
hidden_size = 4
batch1 = torch.randn(batch_size, input_size, hidden_size)
batch2 = torch.randn(batch_size, hidden_size, input_size)
output = torch.Tensor.addbmm(batch1, batch2)
print(output)