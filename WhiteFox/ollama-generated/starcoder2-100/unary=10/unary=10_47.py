
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(240, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0)
        v4  = torch.clamp_max(v3, 6)
        v5  = v4 / 6 
        return v5


# Initializing the model and loading pre-trained weights
m  = Model()
m.load_state_dict(torch.load('model'))

 # Inputs to the model. 
 x1 = torch.randn(20, 32)
 
 # Generating model output using forward pass: 
 __output__  = m(x1)

