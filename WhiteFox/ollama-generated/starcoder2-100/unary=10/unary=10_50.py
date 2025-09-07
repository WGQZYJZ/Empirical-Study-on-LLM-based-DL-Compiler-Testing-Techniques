
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(28 * 28, 10)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + 3
        v3  = F.relu6(v2) 
        v4  = torch.clamp_min(v3, 0) # clamp the output of the addition operation to a minimum of 0
        v5  = torch.clamp_max(v4, 6) # clamp the output of the previous operation to a maximum of 6
        v6  = v5 / 6 # divide the output of the previous operation by 6
        return v6

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(20, 784)

