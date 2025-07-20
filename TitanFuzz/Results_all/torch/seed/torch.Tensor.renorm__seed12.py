input_tensor = torch.randn(4, 4)
p = 2
dim = 0
maxnorm = 1
output_tensor = torch.Tensor.renorm_(input_tensor, p, dim, maxnorm)