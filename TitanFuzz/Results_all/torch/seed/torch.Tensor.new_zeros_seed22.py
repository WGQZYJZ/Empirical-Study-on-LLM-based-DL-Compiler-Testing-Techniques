x = torch.randn(4, 5, requires_grad=True)
y = torch.Tensor.new_zeros(x, size=(4, 5), dtype=torch.float32, device=None, requires_grad=True)