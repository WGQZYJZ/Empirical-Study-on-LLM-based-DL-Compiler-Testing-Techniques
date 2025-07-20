input_tensor = torch.rand(2, 3)
amin_result = torch.Tensor.amin(input_tensor, dim=1, keepdim=False)