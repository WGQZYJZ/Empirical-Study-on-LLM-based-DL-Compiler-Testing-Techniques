input_tensor = torch.rand(5, 5)
kthvalue_result = torch.Tensor.kthvalue(input_tensor, 3, dim=1, keepdim=True)
kthvalue_result = torch.Tensor.kthvalue(input_tensor, 3, dim=1, keepdim=False)