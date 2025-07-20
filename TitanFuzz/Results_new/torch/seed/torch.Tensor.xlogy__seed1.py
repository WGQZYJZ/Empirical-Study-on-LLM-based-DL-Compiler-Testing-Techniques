input_tensor = torch.randn(3, 5, requires_grad=True)
other = torch.randn(3, 5, requires_grad=True)
torch.Tensor.xlogy_(input_tensor, other)