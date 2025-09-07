
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att  = torch.nn.MultiheadAttention(64, 8)
 
    def forward(self, x1, x2):
        v1  = self.att(query=x1, key=x2)[0] # Apply multihead attention to the inputs
        return v1

# Initializing the model
m  = Model()

# Inputs to the model
x1_ = torch.randn(64, 3*8)
x2_ = torch.randn(3, 8, 50, 50)

# Generating an output
m(x1_, x2_)

