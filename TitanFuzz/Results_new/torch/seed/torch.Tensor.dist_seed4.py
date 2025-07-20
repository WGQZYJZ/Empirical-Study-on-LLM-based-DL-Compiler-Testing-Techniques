input_tensor = torch.rand(2, 3)
other = torch.rand(3)
torch.Tensor.dist(input_tensor, other, p=2)