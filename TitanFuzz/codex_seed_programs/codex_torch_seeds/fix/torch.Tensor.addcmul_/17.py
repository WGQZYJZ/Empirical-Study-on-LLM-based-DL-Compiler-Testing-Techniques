'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcmul_\ntorch.Tensor.addcmul_(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
if True:
    input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
    tensor1 = torch.tensor([[7, 8, 9], [10, 11, 12]], dtype=torch.float32)
    tensor2 = torch.tensor([[13, 14, 15], [16, 17, 18]], dtype=torch.float32)
    input_tensor.addcmul_(tensor1, tensor2)
    print('Input tensor: ', input_tensor)
    print('Tensor1: ', tensor1)
    print('Tensor2: ', tensor2)