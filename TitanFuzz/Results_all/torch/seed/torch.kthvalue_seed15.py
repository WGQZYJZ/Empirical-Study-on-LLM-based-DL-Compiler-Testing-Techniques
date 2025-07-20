input_tensor = torch.randn(2, 3, 4)
(output_tensor, index) = torch.kthvalue(input_tensor, 2, dim=1)