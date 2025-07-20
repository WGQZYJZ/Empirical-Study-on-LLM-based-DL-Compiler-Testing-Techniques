buffer = bytearray(4)
buffer[0] = 1
buffer[1] = 2
buffer[2] = 3
buffer[3] = 4
buffer_tensor = torch.frombuffer(buffer, dtype=torch.int8)
buffer_tensor = torch.frombuffer(buffer, dtype=torch.int8, count=3)
buffer_tensor = torch.frombuffer(buffer, dtype=torch.int8, count=3, offset=1)