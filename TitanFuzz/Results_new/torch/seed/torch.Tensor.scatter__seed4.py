input_tensor = torch.rand(4, 3)
index = torch.tensor([[0, 1, 2, 0], [2, 0, 0, 1]])
src = torch.tensor([3.1415, 2.7182])
output_tensor = torch.Tensor.scatter_(input_tensor, 0, index, src)