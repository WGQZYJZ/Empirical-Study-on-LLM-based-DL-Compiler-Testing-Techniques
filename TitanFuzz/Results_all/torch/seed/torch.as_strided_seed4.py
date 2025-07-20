input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
size = (2, 2)
stride = (1, 2)
storage_offset = 0
output = torch.as_strided(input, size, stride, storage_offset)