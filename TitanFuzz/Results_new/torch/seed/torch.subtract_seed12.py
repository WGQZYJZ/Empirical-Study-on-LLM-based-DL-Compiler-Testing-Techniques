tensor_a = torch.rand(3, 3)
tensor_b = torch.rand(3, 3)
tensor_c = torch.subtract(tensor_a, tensor_b)
tensor_c = torch.subtract(tensor_a, tensor_b, alpha=2)