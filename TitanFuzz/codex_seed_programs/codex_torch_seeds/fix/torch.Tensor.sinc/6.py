'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sinc\ntorch.Tensor.sinc(_input_tensor)\n'
import torch
import numpy as np
input_data = np.array([(- 2), (- 1), 0, 1, 2])
output_data = torch.Tensor.sinc(torch.Tensor(input_data))
print(output_data)