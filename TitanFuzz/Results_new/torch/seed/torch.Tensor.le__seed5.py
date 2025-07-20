input_tensor = torch.randn(2, 3, 4)
other = torch.randn(2, 3, 4)
out = torch.Tensor.le_(input_tensor, other)