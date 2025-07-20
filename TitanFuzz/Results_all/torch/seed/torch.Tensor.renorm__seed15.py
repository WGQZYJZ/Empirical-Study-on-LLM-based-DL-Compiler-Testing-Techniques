input_tensor = torch.randn(2, 3, 4)
torch.Tensor.renorm_(input_tensor, p=1, dim=1, maxnorm=2)