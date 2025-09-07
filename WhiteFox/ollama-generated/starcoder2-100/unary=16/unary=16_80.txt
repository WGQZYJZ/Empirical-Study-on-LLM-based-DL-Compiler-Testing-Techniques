

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin  = torch.nn.Linear(32 * 64, 8)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = F.relu(v1) 
        return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(32 * 64, 8).to(device)

# Initializing loss function
loss_fn = nn.MSELoss(reduction='mean')

 # Initializing optimizer for the weights of the model
optim = optim.AdamW([{'params':m.lin.parameters()}], lr=0.1)

# Computing output from the model
__output__  = m(x1) 

# Compute loss
loss = loss_fn(__output__, torch.zeros_like(__output__).to(device))

# Compute backward and update weights of the model
optim.zero_grad()
loss.backward()

 optim.step()
