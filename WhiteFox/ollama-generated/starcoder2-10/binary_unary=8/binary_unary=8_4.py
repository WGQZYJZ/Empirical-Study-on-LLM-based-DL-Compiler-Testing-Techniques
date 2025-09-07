
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 10 # added by Yuya
        v3  = torch.relu(v2) # add another ReLU to the output of the pointwise convolution with 1
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

# Initializing the optimizer
optimizer  = torch.optim.SGD(m.parameters(), lr=0.1) # added by Yuya

# Training loop for one epoch with automatic backward call, and printing results after every iteration (or batch) to stdout.
for i in range(15):
    loss  = F.mse_loss(m(x1), torch.ones([320])) # added by Yuya
    optimizer.zero_grad() 
    loss.backward() # backward call
    optimizer.step()  # step() call
    if (i % 4) == 0:
        print(f'Step {i}, Loss = {loss}')

# Initializing the model with default settings, and then training for one epoch with automatic backward call, and printing results after every iteration (or batch) to stdout.
m2  = Model() # Yuya - original code: m  = Model(args)
for i in range(15):
    loss = F.mse_loss(m(x1), torch.ones([320]))  
    optimizer.zero_grad() 
    loss.backward() # backward call
    optimizer.step()  # step() call
    if (i % 4) == 0:
        print(f'Step {i}, Loss = {loss}')

# Initializing the model with default settings, and then training for one epoch with automatic backward call, printing loss after every iteration to stdout.
m2  = Model() # Yuya - original code: m  = Model(args)
for i in range(15):
    optimizer.zero_grad() 
    loss  = F.mse_loss(m(x1), torch.ones([320]))  
    loss.backward() # backward call
    optimizer.step()  # step() call
    print(f'Step {i}, Loss = {loss}')
