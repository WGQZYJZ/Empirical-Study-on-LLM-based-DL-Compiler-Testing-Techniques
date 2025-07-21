'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_sparse\ntorch.Tensor.to_sparse(_input_tensor, sparseDims)\n'
import torch
import torch
input_tensor = torch.randn(10, 10, requires_grad=True)
output_tensor = input_tensor.to_sparse()
print(output_tensor)