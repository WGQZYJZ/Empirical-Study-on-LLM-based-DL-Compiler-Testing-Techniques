input_tensor = torch.rand(2, 3, 4)
output_tensor = torch.Tensor.gather(input_tensor, dim=1, index=torch.tensor([[0, 1, 2], [2, 0, 1]]))