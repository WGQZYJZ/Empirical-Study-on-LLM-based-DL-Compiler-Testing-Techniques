'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.seed\ntorch.random.seed()\n'
import torch
(N, D_in, H, D_out) = (64, 1000, 100, 10)
x = torch.randn(N, D_in)
y = torch.randn(N, D_out)
torch.random.seed()
model = torch.nn.Sequential(torch.nn.Linear(D_in, H), torch.nn.ReLU(), torch.nn.Linear(H, D_out))
loss_fn = torch.nn.MSELoss(reduction='sum')
learning_rate = 0.0001
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)