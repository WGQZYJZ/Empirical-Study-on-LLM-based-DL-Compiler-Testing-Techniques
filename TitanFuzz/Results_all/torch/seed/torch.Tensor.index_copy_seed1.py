input_tensor = torch.rand(3, 3)
dim = 0
index = torch.tensor([0, 2])
tensor2 = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.Tensor.index_copy(input_tensor, dim, index, tensor2)