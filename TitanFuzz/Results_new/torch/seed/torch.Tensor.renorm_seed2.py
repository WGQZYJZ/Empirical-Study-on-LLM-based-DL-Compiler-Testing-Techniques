input_tensor = torch.randn(2, 3, 4)
output_tensor = torch.Tensor.renorm(input_tensor, p=2, dim=1, maxnorm=5.0)
input_tensor = torch.randn(2, 3, 4)