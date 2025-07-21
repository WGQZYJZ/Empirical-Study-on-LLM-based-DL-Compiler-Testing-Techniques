'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.baddbmm_\ntorch.Tensor.baddbmm_(_input_tensor, batch1, batch2, *, beta=1, alpha=1)\n'
import torch
batch_size = 3
input_size = 2
output_size = 4
input_tensor = torch.randn(batch_size, input_size)
batch1 = torch.randn(batch_size, input_size, output_size)
batch2 = torch.randn(batch_size, output_size, input_size)
output_tensor = input_tensor.baddbmm_(batch1, batch2)
print(output_tensor)