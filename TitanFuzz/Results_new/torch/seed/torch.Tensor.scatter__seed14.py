input_tensor = torch.randn(3, 4)
index = torch.tensor([[0, 1, 2, 0], [2, 0, 0, 1]])
src = torch.tensor([[1, 0, (- 1), 1], [1, (- 1), 1, 0]])
output_tensor = torch.Tensor.scatter_(input_tensor, dim=0, index=index, src=src)