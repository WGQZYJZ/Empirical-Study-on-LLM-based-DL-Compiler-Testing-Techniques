input_tensor = torch.randn(3, 4)
logcumsumexp_tensor = torch.Tensor.logcumsumexp(input_tensor, dim=1)