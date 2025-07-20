input_data = torch.randint(low=1, high=10, size=(4, 4), dtype=torch.int32)
other_data = torch.randint(low=1, high=10, size=(4, 4), dtype=torch.int32)
remainder_data = torch.remainder(input=input_data, other=other_data)