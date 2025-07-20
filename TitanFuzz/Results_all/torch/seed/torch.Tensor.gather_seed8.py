input_tensor = torch.randn(2, 3)
dim = 0
index = torch.tensor([0, 1])
output_tensor = torch.Tensor.gather(input_tensor, dim, index)