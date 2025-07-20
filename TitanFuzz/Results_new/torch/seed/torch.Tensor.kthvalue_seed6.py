input_tensor = torch.randn(2, 3, 4)
k = 1
dim = 0
keepdim = True
output = torch.Tensor.kthvalue(input_tensor, k, dim, keepdim)