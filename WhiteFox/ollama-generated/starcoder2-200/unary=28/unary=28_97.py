
class Model(torch.nn.Module):
    def __init__(self, min_value=0., max_value=1.):
        super().__init__()
        self.linear  = torch.nn.Linear(256, 3)

    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, min_value) 
        v3  = torch.clamp_max(v2, max_value) 
        return v3

# Initializing the model
m  = Model()
m.__init__(min_value=-0.5, max_value=2.)

 # Inputs to the model
x1  = torch.randn(64*64*8*8, 256)
 
# Outputs of the model with the inputs
