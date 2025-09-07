
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
      	t1 = torch.nn.functional.dropout(x1, p=0.5)
      	t2 = torch.rand_like(t1)
      	return t1


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(3, 2)


