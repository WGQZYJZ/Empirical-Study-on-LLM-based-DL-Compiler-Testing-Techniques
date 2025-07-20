input_tensor = torch.randn(3, 4, requires_grad=True)
torch.Tensor.retains_grad(input_tensor, True)