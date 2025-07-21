'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dot\ntorch.Tensor.dot(_input_tensor, other)\n'
import torch
_input_tensor = torch.randn(2, 3)
other = torch.randn(3, 2)
torch.Tensor.dot(_input_tensor, other)
'\nTask 4: Call the API torch.dot\ntorch.dot(_input_tensor.view(-1), other.view(-1))\n'
torch.dot(_input_tensor.view((- 1)), other.view((- 1)))
'\nTask 5: Call the API torch.matmul\ntorch.matmul(_input_tensor, other)\n'
torch.matmul(_input_tensor, other)
'\nTask 6: Call the API torch.mm\ntorch.mm(_input_tensor, other)\n'
torch.mm(_input_tensor, other)
'\nTask 7: Call the API torch.bmm\ntorch.bmm(_input_tensor.unsqueeze(0), other.unsqueeze(0))\n'