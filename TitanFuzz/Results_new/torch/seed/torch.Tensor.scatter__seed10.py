input_tensor = torch.randn(3, 4)
index = torch.tensor([0, 1, 1, 2])
src = torch.randn(4)
output_tensor = torch.Tensor.scatter_(input_tensor, dim=0, index=index, src=src)