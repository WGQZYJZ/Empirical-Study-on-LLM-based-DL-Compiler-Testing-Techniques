'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.fractional_max_pool2d\ntorch.nn.functional.fractional_max_pool2d(*args, **kwargs)\n'
import torch
import torch.nn.functional as F
if True:
    import torch
    input = torch.randn(1, 1, 5, 5)
    output = F.fractional_max_pool2d(input, (3, 3), output_size=(3, 3))
    print(output)