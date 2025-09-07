
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(3, 4)

    def forward(self, x1): 
        v1  = self.l1(x1) + 3
        v2  = torch.clamp_min(v1, 0) # Clamp the output of the addition operation to a minimum of 0
        v3  = torch.clamp_max(v2, 6) # Clamp the output of the previous operation to a maximum of 6
        v4  = v3 / 6 # Divide the output of the previous operation by 6 
        return v4

# Initializing the model 
m  = Model()

# Input tensor x1
x1  = torch.randn(1, 3)


