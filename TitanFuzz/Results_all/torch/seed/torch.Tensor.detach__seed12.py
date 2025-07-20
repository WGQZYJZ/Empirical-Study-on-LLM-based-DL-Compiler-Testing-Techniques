input_tensor = torch.randn(5, 7, requires_grad=True)
detached_tensor = torch.Tensor.detach_(input_tensor)