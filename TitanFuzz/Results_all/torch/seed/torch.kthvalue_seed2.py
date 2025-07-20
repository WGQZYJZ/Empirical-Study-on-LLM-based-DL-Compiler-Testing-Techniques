input_data = torch.randn(10, 5)
k = 3
result = torch.kthvalue(input_data, k)
result = torch.kthvalue(input_data, k, dim=0)
result = torch.kthvalue(input_data, k, dim=1)
result = torch.kthvalue(input_data, k, dim=(- 1))
result = torch.kthvalue(input_data, k, dim=1, keepdim=True)
result = torch.kthvalue(input_data, k, dim=(- 1), keepdim=True)