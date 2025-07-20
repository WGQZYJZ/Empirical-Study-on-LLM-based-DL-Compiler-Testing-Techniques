input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float32)
output_tensor = torch.Tensor.nanmedian(input_tensor, dim=1, keepdim=True)