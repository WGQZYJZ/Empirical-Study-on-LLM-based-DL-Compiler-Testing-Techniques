
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        l1 = torch.nn.functional.linear(x1)
        l2 = l1 + 3
        l3 = torch.clamp_min(l2, 0)
        l4 = torch.clamp_max(l3, 6)
        l5 = l4 / 6
        return l5


# Initializing the model and generating the input tensor to it
m1  = Model()
x1 = torch.randn(1, 9217)
 
# Calling the model with the given input
__output__  = m1(x1)