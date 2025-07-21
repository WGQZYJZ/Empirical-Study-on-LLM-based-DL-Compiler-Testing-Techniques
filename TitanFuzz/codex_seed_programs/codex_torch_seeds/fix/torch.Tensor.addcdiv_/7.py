'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcdiv_\ntorch.Tensor.addcdiv_(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
input_tensor = torch.randn(4, 4)
tensor1 = torch.randn(4, 4)
tensor2 = torch.randn(4, 4)
tensor3 = torch.Tensor.addcdiv_(input_tensor, tensor1, tensor2, value=1)
print('input_tensor:', input_tensor)
print('tensor1:', tensor1)
print('tensor2:', tensor2)
print('tensor3:', tensor3)