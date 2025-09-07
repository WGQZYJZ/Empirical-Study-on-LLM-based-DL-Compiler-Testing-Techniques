
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        layer1_output = self.layer1(x1)
        return layer1_output * 0.5


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
