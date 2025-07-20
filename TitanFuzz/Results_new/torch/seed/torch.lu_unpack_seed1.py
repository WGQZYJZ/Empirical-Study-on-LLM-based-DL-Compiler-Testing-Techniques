A = torch.tensor([[1.0, 2.0, 3.0], [3.0, 4.0, 5.0], [5.0, 6.0, 7.0]])
(LU_data, LU_pivots) = torch.lu(A)
torch.lu_unpack(LU_data, LU_pivots, unpack_data=True, unpack_pivots=True)