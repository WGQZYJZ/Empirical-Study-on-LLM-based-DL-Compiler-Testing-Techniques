
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other  # <- this is added tensor 
        v3  = F.relu(v2)  # <- Relu activation
        return v3


# Initializing the model with keyword argument `other` set to a randomly generated tensor of shape `(4,)` and filled with numbers uniformly sampled between `-0.1` and `0.1`.
m = Model()
other_rand  = torch.empty(4).uniform_(-0.1, .1)
__output__  = m(x1, other=other_rand)

