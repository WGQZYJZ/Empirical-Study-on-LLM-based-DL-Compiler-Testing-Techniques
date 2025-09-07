
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32*32*3, 512)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1  = self.linear(x1.view(-1, 3 * 32 * 32))
        return self.relu(v1), x1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4096, 32*32*3)
x2 = torch.randn(3, 32*32*3)

# Outputs of the model
__output1__, __output2__ = m(x1), m(x2)

