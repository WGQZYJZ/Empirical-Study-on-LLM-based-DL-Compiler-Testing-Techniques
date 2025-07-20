input_data = torch.randn(1, 1, 3, 3)
input_data.requires_grad = True
softplus = torch.nn.Softplus(beta=1, threshold=20)
output_data = softplus(input_data)