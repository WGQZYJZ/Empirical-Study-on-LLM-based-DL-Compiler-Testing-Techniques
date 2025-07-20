input_tensor = torch.randn(4, 4)
dim = 1
index = torch.tensor([0, 2])
tensor = torch.randn(2, 4)
torch.Tensor.index_copy_(input_tensor, dim, index, tensor)