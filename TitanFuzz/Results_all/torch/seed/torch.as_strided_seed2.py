input = torch.tensor([[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]])
size = [2, 3, 2]
stride = [4, 2, 1]
storage_offset = 0
output = torch.as_strided(input, size, stride, storage_offset)