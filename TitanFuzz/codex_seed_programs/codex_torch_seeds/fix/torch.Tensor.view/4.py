'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.view\ntorch.Tensor.view(_input_tensor, *shape)\n'
import torch
import torch
in_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
out_tensor = in_tensor.view(3, 2)
print(out_tensor)