A = torch.rand(3, 3)
lu_result = torch.lu(A, pivot=True, get_infos=True)