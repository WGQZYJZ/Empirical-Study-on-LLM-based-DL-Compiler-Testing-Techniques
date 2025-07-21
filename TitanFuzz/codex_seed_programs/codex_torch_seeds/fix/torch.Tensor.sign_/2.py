'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sign_\ntorch.Tensor.sign_(_input_tensor)\n'
import torch
input_tensor = torch.rand(4, 4)
torch.Tensor.sign_(input_tensor)
print(input_tensor)
out_tensor = torch.rand(4, 4)
torch.Tensor.sign_(input_tensor, out=out_tensor)
print(out_tensor)
torch.sign(input_tensor)