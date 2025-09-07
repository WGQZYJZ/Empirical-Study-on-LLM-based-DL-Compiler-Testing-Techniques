
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8 * 64, 12)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v3  = v1 - other
        v5  = F.relu(v3)
        return v5


# Initializing the model
m  = Model()

 # Inputs to the model
other = 0.7692837471736574
x1  = torch.randn(2, 10 * 64)
 
 __output__  = m(x1)
