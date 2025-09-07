
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear1 = torch.nn.Linear(32, 48)
        self.other = torch.nn.Parameter(
            data=torch.zeros([48]),
            requires_grad=True,
        )
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        return v1 + other

# Initializing the model 
m = Model()

 # Inputs to the model 
 x1 = torch.randn(1024*3)
 
 
 