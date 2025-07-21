'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.retains_grad\ntorch.Tensor.retains_grad(_input_tensor, )\n'
import torch
if True:
    import torch
    input_tensor = torch.randn(3, requires_grad=True)
    print(input_tensor)
    torch.Tensor.retains_grad(input_tensor, True)