"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.lr_scheduler.ReduceLROnPlateau\ntorch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode='min', factor=0.1, patience=10, threshold=0.0001, threshold_mode='rel', cooldown=0, min_lr=0, eps=1e-08, verbose=False)\n"
import torch
import torch.optim as optim
input_data = torch.randn(20, 5)
target = torch.randn(20)
model = torch.nn.Linear(5, 1)
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min', factor=0.1, patience=10, verbose=True)
for epoch in range(100):
    optimizer.zero_grad()
    output = model(input_data)
    loss = torch.nn.functional.mse_loss(output, target)
    loss.backward()
    optimizer.step()
    scheduler.step(loss)