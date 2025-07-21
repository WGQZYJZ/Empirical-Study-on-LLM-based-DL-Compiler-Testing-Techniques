'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_xor_\ntorch.Tensor.bitwise_xor_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[1, 0, 1], [0, 1, 0], [1, 0, 1]], dtype=torch.uint8)
other = torch.tensor([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=torch.uint8)
output_tensor = input_tensor.bitwise_xor_(other)
print(output_tensor)