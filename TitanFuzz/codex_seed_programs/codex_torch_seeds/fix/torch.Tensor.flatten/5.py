'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flatten\ntorch.Tensor.flatten(_input_tensor, start_dim=0, end_dim=-1)\n'
import torch
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(input_tensor.flatten())
print(input_tensor.flatten(start_dim=1))
'\nTask 4: Call the API torch.Tensor.reshape\ntorch.Tensor.reshape(_input_tensor, shape)\n'
print(input_tensor.reshape(1, 12))
print(input_tensor.reshape(3, 4))
'\nTask 5: Call the API torch.Tensor.view\ntorch.Tensor.view(_input_tensor, shape)\n'
print(input_tensor.view(1, 12))
print(input_tensor.view(3, 4))