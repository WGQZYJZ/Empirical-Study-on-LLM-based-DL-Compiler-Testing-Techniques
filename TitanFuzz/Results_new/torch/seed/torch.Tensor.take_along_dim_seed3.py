input_tensor = torch.randn(2, 3, 4)
indices = torch.tensor([1, 0, 0, 1])
dim = 1
output_tensor = torch.Tensor.take_along_dim(input_tensor, indices, dim)