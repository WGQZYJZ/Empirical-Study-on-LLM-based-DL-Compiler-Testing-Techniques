
class Model(torch.nn.Module):
    def __init__(self, input_size=257):
        super().__init__()
 
        self.l1 = torch.nn.Linear(input_size, 10)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x):
        l1 = self.l1(x).clamp(min=0, max=6)
        l2 = (l1 + 3).relu() / 6
 
        return l2


# Initializing the model
m  = Model()

 # Inputs to the model
x  = torch.randn(4589731, 257)
 
__output__  = m(x)

