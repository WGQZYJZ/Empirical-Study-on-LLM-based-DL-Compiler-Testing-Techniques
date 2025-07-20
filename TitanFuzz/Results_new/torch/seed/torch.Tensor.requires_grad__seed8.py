input_tensor = torch.rand(3, 3)
torch.Tensor.requires_grad_(input_tensor, requires_grad=True)
torch.Tensor.requires_grad_(input_tensor, requires_grad=False)