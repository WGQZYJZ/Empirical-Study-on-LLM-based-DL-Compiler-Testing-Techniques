mat1 = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
mat2 = torch.tensor([[1, 2], [3, 4], [5, 6]], dtype=torch.float32)
result = torch.Tensor.mm(mat1, mat2)