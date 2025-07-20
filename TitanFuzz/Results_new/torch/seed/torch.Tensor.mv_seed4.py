input_tensor = torch.rand(5, 3)
vec = torch.rand(3)
result = torch.Tensor.mv(input_tensor, vec)