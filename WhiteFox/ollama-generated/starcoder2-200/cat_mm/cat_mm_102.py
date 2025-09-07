
class Model(torch.nn.Module):
    def __init__(self, n_concat):
        super().__init__()
 
    def forward(self, input1, input2):
        v1  = torch.mm(input1, input2)
        return torch.cat([v1] * (3 + self.n_concat), dim=0)


# Initializing the model
m  = Model(5)

# Inputs to the model
x1 = torch.randn(1684, 789)
x2 = torch.randn(789, 3)
