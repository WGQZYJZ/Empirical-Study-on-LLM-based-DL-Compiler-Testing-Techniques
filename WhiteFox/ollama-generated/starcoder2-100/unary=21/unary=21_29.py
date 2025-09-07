
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.tanh(v1)
        return v2
# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
 
 # Initializing optimizer
optimiser_func  = torch.optim.SGD(params=m.parameters(), lr=.05)
 
  # Running the optimisation process for one epoch
optimiser_func.zero_grad()
x1 = m(x1).view(-1, )
optimiser_func.step()

 