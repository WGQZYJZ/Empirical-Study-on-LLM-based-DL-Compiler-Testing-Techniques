
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + 3          # Addition Operation
        v4  = torch.clamp_min(v2, 0)   # Clamp Operation Min = 0
        v5  = torch.clamp_max(v4, 6)    # Clamp Operation Max = 6 
        v7  = v1 * v5            # Multiplication Operation  
        v8  = v7 / 6           # Division Operation
        return v8

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 20, 20)


# Initializing optimizer
opt = torch.optim.Adam(m.parameters())

# Training loop (equivalent to calling train(), but allows for different learning rates and momentum)
for epoch in range(1):
    for i in range(num_epochs):
        for j, batch in enumerate(dataloader):
            x, y  = batch
            opt.zero_grad()

            # Forward pass
            __output__  = m(x)
            loss        = F.mse_loss(__output__, y)

            # Backward pass and optimization step (with gradient accumulation)
            loss / accumulation_steps    # Divide the loss by a variable
            loss.backward()
            opt.step()

