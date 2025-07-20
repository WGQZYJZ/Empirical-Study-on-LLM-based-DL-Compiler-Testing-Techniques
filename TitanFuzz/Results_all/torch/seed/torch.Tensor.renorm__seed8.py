input_tensor = torch.randn(3, 4)
torch.Tensor.renorm_(input_tensor, p=2, dim=1, maxnorm=1)