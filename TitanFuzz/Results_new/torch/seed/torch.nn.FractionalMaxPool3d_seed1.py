input_tensor = torch.randn(20, 16, 50, 32, 45)
torch.nn.FractionalMaxPool3d(kernel_size=(5, 10, 3), output_size=(5, 5, 5))(input_tensor)