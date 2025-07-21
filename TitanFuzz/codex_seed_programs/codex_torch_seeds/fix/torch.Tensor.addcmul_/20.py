'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcmul_\ntorch.Tensor.addcmul_(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
tensor1 = torch.tensor([[1, 2], [3, 4]])
tensor2 = torch.tensor([[5, 6], [7, 8]])
tensor3 = torch.tensor([[9, 10], [11, 12]])
torch.Tensor.addcmul_(tensor1, tensor2, tensor3)
print(tensor1)