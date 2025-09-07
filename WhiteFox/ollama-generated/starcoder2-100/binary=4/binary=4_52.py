
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256 * 384 + 1000, 79)

    def forward(self, x1, x2):
        x1_flat = torch.flatten(x1)

        v1 = torch.cat((x1_flat, other))
        v2 = self.linear(v1)
        return v2


# Initializing the model 
m = Model()
 
 # Inputs to the model 
 x1 = torch.randn(800, 384, 56, 56) 
 other = torch.randn(79)
 __output__  = m(x1, other)

