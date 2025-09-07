
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 16, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1) + torch.randn((100, 32 * 16), requires_grad=True)
        return v1


# Initializing the model
m = Model()


