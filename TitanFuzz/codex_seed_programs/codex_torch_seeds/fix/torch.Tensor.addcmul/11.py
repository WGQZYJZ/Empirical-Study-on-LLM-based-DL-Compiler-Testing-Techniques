'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addcmul\ntorch.Tensor.addcmul(_input_tensor, tensor1, tensor2, *, value=1)\n'
import torch
if True:
    input_tensor = torch.randn(4, 4)
    tensor1 = torch.randn(4, 4)
    tensor2 = torch.randn(4, 4)
    output_tensor = torch.Tensor.addcmul(input_tensor, tensor1, tensor2)
    print(output_tensor)