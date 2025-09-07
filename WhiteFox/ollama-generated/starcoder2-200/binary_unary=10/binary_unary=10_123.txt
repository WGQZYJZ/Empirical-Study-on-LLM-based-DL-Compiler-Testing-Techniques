
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64* 64 * 3, 8)

    def forward(self, x1):
       return F.relu(x + other_tensor)

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1, 64, 64, 3)

# Other tensor that will be added with the linear transformation of x1 and input to model m:
other_tensor = torch.randn(1,8)

 __output__=m(x1)
