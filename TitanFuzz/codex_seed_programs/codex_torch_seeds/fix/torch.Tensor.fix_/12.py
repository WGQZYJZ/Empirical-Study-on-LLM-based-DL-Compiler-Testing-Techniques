'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fix_\ntorch.Tensor.fix_(_input_tensor)\n'
import torch
input = torch.rand(1, 3, 224, 224)
torch.Tensor.fix_(input)
print(input)