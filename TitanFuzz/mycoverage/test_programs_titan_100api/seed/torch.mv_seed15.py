input_data = torch.randn(2, 3)
vec = torch.tensor([1, 0, (- 1)], dtype=torch.float)
output = torch.mv(input_data, vec)