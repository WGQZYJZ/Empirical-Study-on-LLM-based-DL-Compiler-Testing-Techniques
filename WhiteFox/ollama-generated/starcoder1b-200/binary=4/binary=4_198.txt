
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(20, 30)
 
    def forward(self, x):
        v1 = self.linear1(x)
        v2 = v1 + other  # Add another tensor to the output of the linear transformation
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(4, 20)
