'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.retains_grad\ntorch.Tensor.retains_grad(_input_tensor, )\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
torch.Tensor.retains_grad(input_tensor, False)
print(input_tensor.requires_grad)