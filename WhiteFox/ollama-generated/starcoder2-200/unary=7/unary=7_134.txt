
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x):
        l1  = self.linear(x)
        l2  = l1 * F.clamp(min=0, max=6, input=l1 + 3)
        l3  = l2 / 6

# Initializing the model
m  = Model()

 # Inputs to the model