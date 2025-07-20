input_tensor = torch.randn(1, 6)
index = torch.tensor([[4, 1, 2, 5]])
src = torch.tensor([[10, 20, 30, 40]])
output_tensor = torch.Tensor.scatter(input_tensor, 0, index, src)