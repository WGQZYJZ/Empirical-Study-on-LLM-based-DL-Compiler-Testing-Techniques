'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.quantize_per_tensor\ntorch.quantize_per_tensor(input, scale, zero_point, dtype)\n'
import torch
import numpy as np
from torch.autograd import Variable
import torch
import numpy as np
input = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float32)
input = torch.from_numpy(input)
input_q = torch.quantize_per_tensor(input, scale=0.5, zero_point=2, dtype=torch.quint8)
print(input_q)
print(input_q.dequantize())