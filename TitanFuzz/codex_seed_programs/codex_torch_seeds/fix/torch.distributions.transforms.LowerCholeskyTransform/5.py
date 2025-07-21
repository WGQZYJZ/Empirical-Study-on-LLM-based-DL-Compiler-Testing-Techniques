'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.LowerCholeskyTransform\ntorch.distributions.transforms.LowerCholeskyTransform(cache_size=0)\n'
import torch
import torch.distributions.transforms as transforms
input_tensor = torch.randn(2, 2)
input_tensor = (input_tensor.t() @ input_tensor)
lower_cholesky_transform = transforms.LowerCholeskyTransform()
lower_cholesky_inv = lower_cholesky_transform.inv(input_tensor)
print(lower_cholesky_inv)