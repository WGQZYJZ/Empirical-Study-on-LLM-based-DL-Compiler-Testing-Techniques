_input_tensor = torch.rand(2, 2)
output_tensor = torch.Tensor.eig(_input_tensor, eigenvectors=False)