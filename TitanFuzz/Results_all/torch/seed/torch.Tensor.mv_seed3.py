input_tensor = torch.arange(1, 7).reshape(2, 3)
vec = torch.arange(1, 4)
result = torch.Tensor.mv(input_tensor, vec)