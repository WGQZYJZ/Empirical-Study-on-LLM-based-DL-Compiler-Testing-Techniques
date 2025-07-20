input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.renorm(input_tensor, p=2, dim=0, maxnorm=1)