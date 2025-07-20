input_data = torch.randn(1, 2, 3, 4, 5)
futures = [torch.futures.Future(), torch.futures.Future()]
futures[0].set_result(input_data)
futures[1].set_result(input_data)
torch.futures.wait_all(futures)