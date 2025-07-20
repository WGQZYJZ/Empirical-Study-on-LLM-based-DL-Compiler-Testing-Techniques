input_tensor = torch.randn(2, 3)
output_tensor = torch.Tensor.gather(input_tensor, dim=1, index=torch.tensor([0, 0]))
output_tensor = torch.Tensor.gather(input_tensor, dim=1, index=torch.tensor([2, 2]))
output_tensor = torch.Tensor.gather(input_tensor, dim=0, index=torch.tensor([0, 0]))