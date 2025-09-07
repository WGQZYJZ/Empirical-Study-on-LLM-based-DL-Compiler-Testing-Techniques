

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(1, 10)
 
    def forward(self, input1):
        v1 = self.mm(input1) + 5
        return v1

# Initializing the model
m = Model()

# Inputs to the model
__input__ = torch.randn(3, 200)

