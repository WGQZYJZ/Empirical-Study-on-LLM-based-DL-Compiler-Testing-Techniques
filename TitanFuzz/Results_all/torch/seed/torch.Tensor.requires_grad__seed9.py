input_tensor = torch.randn(2, 3, requires_grad=True)
torch.Tensor.requires_grad_(input_tensor, requires_grad=True)
torch.Tensor.requires_grad_(input_tensor, requires_grad=False)