
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + 3 # add 3 to the output of the linear transformation
        v3  = torch.clamp_min(v2, min=0) # clamp the output of the addition operation to a minimum of 0
        v4  = torch.clamp_max(v3, max=6) # clamp the output of the previous operation to a maximum of 6
        v5  = v4 / 6 # divide the output of the previous operation by 6
        return v5

# Initializing the model
m = Model()
