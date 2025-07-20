A = torch.randn(3, 2)
b = torch.randn(3)
x = torch.Tensor.lstsq(b, A)