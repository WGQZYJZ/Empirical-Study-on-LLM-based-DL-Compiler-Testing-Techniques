
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1) * 0.5
        v2 = torch.cat((torch.randn(3, 2), 
                          torch.randn(3, 1)), 0)
        v3 = torch.cat((v1 + v1, 
                          torch.ones(3, 2)), 0) * 0.044715
        v4 = torch.cat((v3 * v3, 
                          torch.zeros(3, 1))), 0)
        v5 = v2 * v4
        return torch.tanh(v5)


# Initializing the model
m = Model()


