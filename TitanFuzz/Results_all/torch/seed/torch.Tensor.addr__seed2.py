input_tensor = torch.rand(3, 3)
vec1 = torch.rand(3)
vec2 = torch.rand(3)
torch.Tensor.addr_(input_tensor, vec1, vec2, beta=1, alpha=1)