'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_tensor\ntorch.quantize_per_tensor(input, scale, zero_point, dtype)\n'
import torch
from torch.quantization import QuantStub, DeQuantStub
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.quantize_per_tensor')
X = torch.tensor([(- 2.0), (- 1.0), 0.0, 1.0, 2.0], dtype=torch.float)
qX = torch.quantize_per_tensor(X, scale=0.5, zero_point=2, dtype=torch.quint8)
print('\nQuantized tensor:\n', qX)
print("\nQuantized tensor's scale and zero point:\n", qX.q_scale(), qX.q_zero_point())
dqX = qX.dequantize