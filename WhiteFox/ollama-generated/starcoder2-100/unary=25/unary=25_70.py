
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).to(torch.float32)
        v3 = v1 * -2.89764e-2
        v4 = torch.where((v2 == True), v1, v3)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(10, 5).to(torch.float32)

