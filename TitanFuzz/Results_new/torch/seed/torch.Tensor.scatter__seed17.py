input_tensor = torch.randn(2, 3)
index = torch.tensor([[0, 1, 0], [1, 0, 1]])
src = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
torch.Tensor.scatter_(input_tensor, dim=0, index=index, src=src)