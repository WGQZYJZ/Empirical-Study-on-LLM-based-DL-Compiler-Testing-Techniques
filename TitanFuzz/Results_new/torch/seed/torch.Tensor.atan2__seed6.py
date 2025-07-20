if True:
    import torch
    input_tensor = torch.rand(3, 3)
    other = torch.rand(3, 3)
    torch.Tensor.atan2_(input_tensor, other)