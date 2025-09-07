
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.m1 = torch.nn.Linear(512, 512)
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2) # Matrix multiplication between input1 and input2
        return v1

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(256) 
x2 = torch.randn(256) 
