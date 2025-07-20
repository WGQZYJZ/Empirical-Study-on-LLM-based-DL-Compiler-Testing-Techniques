input_tensor = torch.randn(2, 3, 5)
torch.Tensor.renorm(input_tensor, p=2, dim=1, maxnorm=1)