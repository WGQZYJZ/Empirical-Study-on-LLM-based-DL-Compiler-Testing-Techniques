
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 4)
 
    def forward(self, x1):
        l1 = self.linear(x1) 
        l2 = l1 * torch.clamp(min=0, max=6, input=l1 + 3) # clamped output of the linear transformation added with 3
        l3 = l2 / 6 # Divide the output of the multiplication by 6
        return l3


# Initializing the model and passing inputs to it.
m  = Model()
x1 = torch.randn(5, 20)
__output__  = m(x1)

