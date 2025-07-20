input_data = torch.randn(1, 2, 3, 4, 5)
to_type = torch.float32
can_cast = torch.can_cast(from_type, to_type)