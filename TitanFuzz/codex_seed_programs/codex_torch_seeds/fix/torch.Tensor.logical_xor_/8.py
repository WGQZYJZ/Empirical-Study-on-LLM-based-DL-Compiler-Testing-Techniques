'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_xor_\ntorch.Tensor.logical_xor_(_input_tensor, other)\n'
import torch
input_tensor1 = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.bool)
input_tensor2 = torch.tensor([[0, 1], [1, 0], [1, 1], [0, 0]], dtype=torch.bool)
torch.Tensor.logical_xor_(input_tensor1, input_tensor2)
print(input_tensor1)