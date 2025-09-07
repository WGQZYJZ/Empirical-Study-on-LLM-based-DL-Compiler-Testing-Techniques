
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4096 + 57, 13)

    def forward(self, x1):
      v1 = self.linear(x1) 
      return relu(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(640, 9752 + 38)


