
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = torch.tanh(v1)

        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

# Initializing a PyTorch optimizer and criterion
optimizer  = torch.optim.Adam(m.parameters(), lr=0.001)
criterion  = torch.nn.MSELoss()

# Training the model
for epoch in range(2):
    for i, batch_X in enumerate(batching process of X input data):
        optimizer.zero_grad()

        yhat  = m(batch_X)
        loss  = criterion(yhat, batch_Y) # Forward pass
        loss.backward() # Backward pass
        optimizer.step() # Update the parameters
        print(loss)


## Training and testing using PyTorch