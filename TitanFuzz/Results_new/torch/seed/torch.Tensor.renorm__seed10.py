input_tensor = torch.randn(4, 3)
output_tensor = torch.Tensor.renorm_(input_tensor, p=2, dim=1, maxnorm=1)