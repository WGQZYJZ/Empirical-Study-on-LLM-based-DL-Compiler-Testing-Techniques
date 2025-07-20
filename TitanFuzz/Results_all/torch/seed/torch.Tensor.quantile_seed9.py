input_tensor = torch.randn(4, 4)
q = 0.5
dim = 0
keepdim = False
output = torch.Tensor.quantile(input_tensor, q, dim, keepdim)