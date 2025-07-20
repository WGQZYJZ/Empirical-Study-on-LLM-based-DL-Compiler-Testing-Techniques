input_tensor = torch.randn(2, 3)
is_shared = torch.Tensor.is_shared(input_tensor)