torch.set_num_threads(2)
x = torch.rand(5000, 5000)
y = torch.rand(5000, 5000)
start_time = time.time()
for i in range(10):
    res = torch.mm(x, y)