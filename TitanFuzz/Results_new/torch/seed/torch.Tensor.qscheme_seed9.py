if True:
    import torch
    input_tensor = torch.rand(1, 3, 224, 224)
    torch.Tensor.qscheme(input_tensor)