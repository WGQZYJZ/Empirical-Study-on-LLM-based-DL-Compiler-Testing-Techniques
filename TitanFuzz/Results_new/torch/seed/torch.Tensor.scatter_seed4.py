_input_tensor = torch.randn(2, 3)
dim = 0
index = torch.tensor([1, 0])
src = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
output = torch.Tensor.scatter(_input_tensor, dim, index, src)