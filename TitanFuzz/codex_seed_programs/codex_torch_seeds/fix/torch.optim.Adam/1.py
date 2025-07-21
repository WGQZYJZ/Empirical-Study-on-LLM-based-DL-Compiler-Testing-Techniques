'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adam\ntorch.optim.Adam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0, amsgrad=False)\n'
import torch
input_data = torch.tensor([[0.0], [1.0], [2.0], [3.0], [4.0]])
target_data = torch.tensor([[0.0], [1.0], [2.0], [3.0], [4.0]])
model = torch.nn.Linear(1, 1)
loss_fn = torch.nn.MSELoss(reduction='sum')
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)