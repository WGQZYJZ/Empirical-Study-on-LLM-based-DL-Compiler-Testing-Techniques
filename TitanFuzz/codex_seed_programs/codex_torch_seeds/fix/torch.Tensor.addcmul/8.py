'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcmul\ntorch.Tensor.addcmul(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
tensor1 = torch.randn(2, 3)
tensor2 = torch.randn(2, 3)
tensor3 = torch.randn(2, 3)
torch.Tensor.addcmul(tensor1, tensor2, tensor3)
print('tensor1:', tensor1)
print('tensor2:', tensor2)
print('tensor3:', tensor3)