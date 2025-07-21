'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addbmm_\ntorch.Tensor.addbmm_(_input_tensor, batch1, batch2, *, beta=1, alpha=1)\n'
import torch
batch_size = 2
input_size = 3
hidden_size = 2
input_tensor = torch.randn(batch_size, input_size)
hidden_tensor = torch.randn(batch_size, hidden_size)
weight_tensor = torch.randn(hidden_size, input_size)
import torch
batch_size = 2
input_size = 3
hidden_size = 2
input_tensor = torch.randn(batch_size, input_size)
hidden_tensor = torch.randn(batch_size, hidden_size)
weight_tensor = torch.randn(hidden_size, input_size)
torch.Tensor.addbmm_(input_tensor, hidden_tensor, weight_tensor, beta=1, alpha=1)
print(input_tensor)