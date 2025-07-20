input_tensor = torch.randn(2, 3)
index = torch.tensor([[0, 1, 0], [1, 0, 1]])
src = torch.tensor([[1, 2, 3], [4, 5, 6]])
output_tensor = torch.Tensor.scatter(input_tensor, 0, index, src)