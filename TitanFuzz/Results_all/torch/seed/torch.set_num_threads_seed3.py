N = 1000
D_in = 100
H = 100
D_out = 10
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)
torch.set_num_threads(4)
model = torch.nn.Sequential(torch.nn.Linear(D_in, H), torch.nn.ReLU(), torch.nn.Linear(H, D_out))
loss_fn = torch.nn.MSELoss(reduction='sum')
learning_rate = 0.0001
start = time.time()
for t in range(500):
    y_pred = model(x)
    loss = loss_fn(y_pred, y)
    print(t, loss.item())