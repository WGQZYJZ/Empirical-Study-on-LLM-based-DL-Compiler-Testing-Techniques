input_tensor = torch.randn(3, 3, requires_grad=True)
vec1 = torch.randn(3, requires_grad=True)
vec2 = torch.randn(3, requires_grad=True)
torch.Tensor.addr_(input_tensor, vec1, vec2, beta=2, alpha=2)