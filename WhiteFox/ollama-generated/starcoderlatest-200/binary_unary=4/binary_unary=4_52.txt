
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        if other is None:
            self.linear = torch.nn.Linear(64*64, 1)
        else:
            self.linear = torch.nn.Linear(64*64, 2)

    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 64*64))
        if not self.training:
          return F.softmax(v1.data, dim=1)
        else:
          return self.linear(x1)

# Initializing the model
m = Model()

 # Inputs to the model
 x1 = torch.randn(2, 3, 64, 64)
 