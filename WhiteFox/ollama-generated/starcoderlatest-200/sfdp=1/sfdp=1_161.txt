
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.Linear(8096, 24)
 
    def forward(self, x1, x2):
        v1 = self.layer1(x1)
        v2 = self.layer2(v1)
        output = v1 * v2
        return output


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8096, 64, 64)
