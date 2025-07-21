'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcmul\ntorch.Tensor.addcmul(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor1 = torch.tensor([[7, 8, 9], [10, 11, 12]])
tensor2 = torch.tensor([[13, 14, 15], [16, 17, 18]])
input_tensor.addcmul(tensor1, tensor2)
print('input_tensor after addcmul: ', input_tensor)