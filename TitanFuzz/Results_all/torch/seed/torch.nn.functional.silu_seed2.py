input_data = torch.arange((- 10), 10, dtype=torch.float32)
output = torch.nn.functional.silu(input_data)