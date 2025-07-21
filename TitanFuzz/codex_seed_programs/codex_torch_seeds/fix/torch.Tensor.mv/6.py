'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mv\ntorch.Tensor.mv(_input_tensor, vec)\n'
import torch
if True:
    import torch
    input_tensor = torch.randn(2, 3)
    vec = torch.tensor([1, 2, 3])
    res = input_tensor.mv(vec)
    print('The result of mv is: ', res)