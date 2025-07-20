input_tensor = torch.randn(3, 4)
index = torch.tensor([[0, 1], [1, 0]])
output_tensor = torch.Tensor.gather(input_tensor, dim=0, index=index)