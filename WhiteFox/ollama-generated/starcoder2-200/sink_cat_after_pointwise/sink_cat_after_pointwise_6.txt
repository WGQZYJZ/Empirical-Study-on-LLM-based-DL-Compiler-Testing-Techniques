
class Model(torch.nn.Module):
    def __init__(self, c1, c2):
        super().__init__()

    def forward(self, x1):
        t1 = torch.cat([x1, self.p], 0) # concat along the first dimension (row-wise concatenation)
        return torch.relu(t1).view(-1)


# Initializing model with fixed parameters
p  = torch.randn(256 * 397 * 438 , 1, 3)

m_init = Model(c1, c2)
__output__   = m(x1)  # This initial model is used for generation

