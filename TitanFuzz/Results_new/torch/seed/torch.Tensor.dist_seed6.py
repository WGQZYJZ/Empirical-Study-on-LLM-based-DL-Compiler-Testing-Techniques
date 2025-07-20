input_tensor = torch.randn(1, 3, 3)
other = torch.randn(1, 3, 3)
result = torch.Tensor.dist(input_tensor, other, p=2)