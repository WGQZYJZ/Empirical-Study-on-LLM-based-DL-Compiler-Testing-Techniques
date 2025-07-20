input_tensor = torch.rand(5, 3)
torch.Tensor.multiply_(input_tensor, 2)
torch.Tensor.multiply_(input_tensor, 3, out=input_tensor)