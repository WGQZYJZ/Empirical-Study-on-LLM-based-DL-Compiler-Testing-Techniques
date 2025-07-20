input_tensor = torch.randn(3, 3, requires_grad=True)
result = torch.Tensor.is_sparse(input_tensor)