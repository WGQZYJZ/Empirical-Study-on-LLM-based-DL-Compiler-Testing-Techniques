input_tensor = torch.randn(3, 5, requires_grad=True)
torch.Tensor.requires_grad_(input_tensor, requires_grad=True)