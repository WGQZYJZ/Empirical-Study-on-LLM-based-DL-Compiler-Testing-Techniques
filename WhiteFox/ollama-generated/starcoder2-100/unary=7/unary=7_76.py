
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*32, 10)
 
    def forward(self, x):
        l1 = self.linear(x)
        l2 = l1 * F.clamp(min=0., max=6., input=l1 + 3.) 
        l3 = torch.div(l2, 6.) # Divide the output of the multiplication by 6
        return l3

# Initializing the model
m  = Model()

