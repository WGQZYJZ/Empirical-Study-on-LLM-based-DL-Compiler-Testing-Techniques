input_tensor = torch.randn(2, 3)
dim = 1
index = torch.tensor([0, 2])
value = 10
output_tensor = torch.Tensor.index_fill(input_tensor, dim, index, value)