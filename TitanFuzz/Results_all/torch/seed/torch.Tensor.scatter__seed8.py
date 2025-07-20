input_tensor = torch.randn(3, 3)
index = torch.tensor([[0, 1, 2], [2, 0, 0]])
src = torch.tensor([3, 4, 5])
output_tensor = torch.Tensor.scatter_(input_tensor, dim=1, index=index, src=src)