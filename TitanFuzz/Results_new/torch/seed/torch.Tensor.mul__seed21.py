input_tensor = torch.Tensor(np.array([[1, 2, 3], [4, 5, 6]]))
scalar = 2
output_tensor = torch.Tensor.mul_(input_tensor, scalar)