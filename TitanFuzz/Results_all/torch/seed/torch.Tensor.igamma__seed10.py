input_tensor = torch.randn(4, 4)
other = torch.randn(4, 4)
output_tensor = torch.Tensor.igamma_(input_tensor, other)
input_tensor = torch.randn(4, 4)
dim = 1
index = torch.tensor([1, 3])
tensor = torch.randn(2, 4)