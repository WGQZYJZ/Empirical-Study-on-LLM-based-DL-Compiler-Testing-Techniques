input_data = [1, 2, 3, 4, 5, 6, 7, 8]
input_tensor = torch.tensor(input_data)
input_storage = torch.QUInt4x2Storage(input_data)
input_storage_from_tensor = torch.QUInt4x2Storage.from_buffer(input_tensor)