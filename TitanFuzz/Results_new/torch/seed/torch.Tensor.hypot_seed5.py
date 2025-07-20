input_tensor = torch.randn(4, 4)
other_tensor = torch.randn(4, 4)
hypot_tensor = torch.Tensor.hypot(input_tensor, other_tensor)
input_tensor = torch.randn(4, 4)
dim = 0
index = torch.tensor([0, 2])