input_data = np.random.rand(1000, 1000)
torch.set_num_threads(1)
start = time.time()
torch.mm(torch.tensor(input_data), torch.tensor(input_data))
end = time.time()