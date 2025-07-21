'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_xor_\ntorch.Tensor.bitwise_xor_(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([[True, False, True], [False, True, False]], dtype=torch.bool)
other_tensor = torch.tensor([[True, True, False], [False, False, True]], dtype=torch.bool)
torch.Tensor.bitwise_xor_(input_tensor, other_tensor)
print('input_tensor = \n', input_tensor)
print('other_tensor = \n', other_tensor)