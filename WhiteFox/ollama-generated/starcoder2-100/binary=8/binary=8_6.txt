
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(2, 3, 64, 64) # Make sure that x1 is of a shape different from m(x1). 
other  = torch.randn_like(x1)


# Initializing the optimizer for the model. In this example we use LBFGS (you can experiment with other optimizers such as SGD, RMSprop or Adam here if you'd like.)
optimizer = torch.optim.LBFGS([p for p in m.parameters() if p.requires_grad], lr=0.5)
 

 # Optimizer loop
 
def closure():
    optimizer.zero_grad()
    __output__  = m(x1)
    __output__.backward()
    return __output__.norm() ** 2 / x1.norm().numel()
 
 
    
for _ in range(50):
    
    optimizer.step(closure)
    
    
