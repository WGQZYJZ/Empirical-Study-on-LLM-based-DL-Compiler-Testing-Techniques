'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract\ntorch.Tensor.subtract(_input_tensor, other, *, alpha=1)\n'
import torch
if True:
    input_tensor = torch.rand(3, 3)
    print(input_tensor)
    output_tensor = torch.Tensor.subtract(input_tensor, 0.5)
    print(output_tensor)