input_tensor = torch.randn(3, 4)
(kth_value, kth_index) = torch.kthvalue(input_tensor, 2, dim=1)
(kth_value, kth_index) = torch.kthvalue(input_tensor, 3, dim=1)
(kth_value, kth_index) = torch.kthvalue(input_tensor, 4, dim=1)