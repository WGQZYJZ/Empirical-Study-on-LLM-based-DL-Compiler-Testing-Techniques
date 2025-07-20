input_tensor = torch.randn(3, 3)
index = torch.tensor([0, 2])
tensor2 = torch.randn(2, 3)
torch.Tensor.index_add(input_tensor, 0, index, tensor2)