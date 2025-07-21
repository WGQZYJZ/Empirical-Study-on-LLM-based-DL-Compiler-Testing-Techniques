'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dequantize\ntorch.Tensor.dequantize(_input_tensor)\n'
import torch
import torch.quantization
import torch.quantization.observer
from torch.quantization import QuantStub, DeQuantStub
from torch.quantization.observer import MovingAverageMinMaxObserver
q_tensor = torch.quantize_per_tensor(torch.tensor([0.0, 1.0, 2.0, 3.0]), 1.0, 0, torch.quint8)
dq_tensor = q_tensor.dequantize()
print(dq_tensor)