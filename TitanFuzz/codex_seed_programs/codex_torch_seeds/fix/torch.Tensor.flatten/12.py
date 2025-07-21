'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flatten\ntorch.Tensor.flatten(_input_tensor, start_dim=0, end_dim=-1)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
print(input_tensor)
print(input_tensor.flatten())
print(input_tensor.flatten(start_dim=1))
print(input_tensor.flatten(start_dim=1, end_dim=2))
'\nTask 4: Call the API torch.Tensor.view\ntorch.Tensor.view(_input_tensor, *shape)\n'
print(input_tensor.view(2, (- 1)))
print(input_tensor.view(2, (- 1)).size())
print(input_tensor.view(2, 12).size())
print(input_tensor.view(24).size())
'\nTask 5: Call the API torch.Tensor.unsqueeze\ntorch.Tensor.unsqueeze(_input_tensor, dim)\n'
print(input_tensor.size())
print(input_tensor.unsqueeze(dim=0).size())