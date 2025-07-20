input_tensor = torch.randn(3, 3)
vec1 = torch.randn(3)
vec2 = torch.randn(3)
torch.Tensor.addr_(input_tensor, vec1, vec2, beta=1, alpha=1)