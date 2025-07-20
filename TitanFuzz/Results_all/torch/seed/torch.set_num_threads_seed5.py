N = 1000000
x = torch.rand(N)
y = torch.rand(N)
torch.set_num_threads(1)
start = time.time()
z = torch.dot(x, y)
end = time.time()