data = bytearray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
tensor = torch.frombuffer(data, dtype=torch.int8, count=5, offset=3)