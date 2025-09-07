
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(in_features=3, out_features=8)
 
    def forward(self, x1):
        v1  = self.linear1(x1) + 2  # Add a number 2 to the output of the linear transformation
        return v1


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3)
