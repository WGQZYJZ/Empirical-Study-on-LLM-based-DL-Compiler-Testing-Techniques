'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.take\ntorch.Tensor.take(_input_tensor, indices)\n'
import torch
import torch
_input_tensor = torch.randint(0, 10, (5, 5))
print(_input_tensor)
print(torch.Tensor.take(_input_tensor, torch.tensor([0, 2, 4])))
print(torch.Tensor.take(_input_tensor, torch.tensor([[0, 2, 4], [1, 3, 4]])))