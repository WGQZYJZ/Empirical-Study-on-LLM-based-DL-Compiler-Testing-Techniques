'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.retain_grad\ntorch.Tensor.retain_grad(_input_tensor)\n'
import torch
import torch
data = torch.randint(0, 10, (3, 2), dtype=torch.float)
print(data)
data.retain_grad()
print(data.grad_fn)