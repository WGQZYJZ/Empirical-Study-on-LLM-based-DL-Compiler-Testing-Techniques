input_1 = torch.randn(2, 3)
input_2 = torch.randn(2, 3, 4)
output = torch.atleast_3d(input_1, input_2)