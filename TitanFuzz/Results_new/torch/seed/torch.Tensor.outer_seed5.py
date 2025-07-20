vec1 = torch.arange(1, 11)
vec2 = torch.arange(11, 21)
result = torch.Tensor.outer(vec1, vec2)