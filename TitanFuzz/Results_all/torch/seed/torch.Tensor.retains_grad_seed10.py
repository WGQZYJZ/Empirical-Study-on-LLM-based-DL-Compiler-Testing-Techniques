input_tensor = torch.randn(10, requires_grad=True)
torch.Tensor.retains_grad(input_tensor, True)