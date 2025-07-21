'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gcd_\ntorch.Tensor.gcd_(_input_tensor, other)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_tensor = torch.randint(low=1, high=10, size=(5, 5), dtype=torch.int32)
print('input_tensor =\n', input_tensor)
print('Task 3: Call the API torch.Tensor.gcd_')
torch.Tensor.gcd_(input_tensor, 3)
print('input_tensor =\n', input_tensor)
'\ntorch.Tensor.gcd_(input, other, out=None) → Tensor\nGreatest common divisor of each value in the input Tensor and other.\nParameters:\n    input (Tensor) – the input tensor\n    other (Number) – the number to compute the gcd with\n    out (Tensor, optional) – the output tensor\nReturns:\n    A Tensor containing the gcd of each value in input and other.\n'