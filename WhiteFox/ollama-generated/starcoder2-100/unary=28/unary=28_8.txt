
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=0.)
        v3 = torch.clamp_max(v2, max=45.99)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(64) # Random input of size (64,) for the linear transformation


# Initializing the model
m2 = Model()


# Inputs to the model
x2  = torch.randn(3, 50).permute([2, 0]).float().cuda()
__output__1  = m(x1) # Calling the model with x1 as input; the output is a tensor of size (64,) and with data type torch.float32 for Model 1
__output__2  = m2(x2).detach().cpu().numpy() # Calling the model with x2 as input; the output is a tensor of size (50, 3) and with data type numpy.ndarray

