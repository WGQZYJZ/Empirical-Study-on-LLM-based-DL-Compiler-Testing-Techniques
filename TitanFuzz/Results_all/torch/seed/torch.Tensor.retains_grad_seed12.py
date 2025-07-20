if True:
    import torch
    input_tensor = torch.randn(3, requires_grad=True)
    print(input_tensor)
    torch.Tensor.retains_grad(input_tensor, True)