
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(x1, x2): # x1 is tensor of dimension 5 and x2 is tensor of dimension 3
      t1 = torch.cat([x1, x2], dim=0)
      t2 = t1.view((t1.shape[0], -1))
      t3 = torch.relu(t2)
      return t3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 2, 2)
x2 = torch.randn(5, 2, 2)
