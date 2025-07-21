input_data = b'\x01\x02\x03\x04'
output = torch.frombuffer(input_data, dtype=torch.uint8, count=4, offset=0)