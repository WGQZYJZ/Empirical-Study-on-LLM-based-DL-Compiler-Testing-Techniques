vec1 = torch.rand(3, dtype=torch.float32)
vec2 = torch.rand(3, dtype=torch.float32)
result = torch.Tensor.outer(vec1, vec2)