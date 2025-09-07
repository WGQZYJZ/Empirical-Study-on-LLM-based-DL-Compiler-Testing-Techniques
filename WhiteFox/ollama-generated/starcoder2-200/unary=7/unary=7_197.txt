

class Model(torch.nn.Module):
    def __init__(self, n1=32):
        super().__init__()
        self.l = torch.nn.Linear(n1, 64*8)
 
    def forward(self, x1):
        l1  = self.l(x1)
        l2  = l1 * (torch.clamp(min=0., max=6.) + 3.) 
        l3  = l2 / 6.
        return l3


# Initializing the model with `n1` equal to 48
m = Model(n1=48)

# Inputs to the model are tensors of dimension (batch_size, 48), where batch_size is not 0
x2 = torch.randn(150, 48)

 