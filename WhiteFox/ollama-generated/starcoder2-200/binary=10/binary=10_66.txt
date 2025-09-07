
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor 
        return v2


# Initializing the model
m = Model()

# Inputs to the model
other_tensor  = torch.randn(5, 8, 64, 32).detach().requires_grad_(True)  # Initialize another tensor with required size and set requires gradient flag as True. 
x1 = torch.randn(10, 9)


# Initializing the model
m = Model()

# Inputs to the model
other_tensor  = torch.randn(5, 8, 64, 32).detach().requires_grad_(True)  # Initialize another tensor with required size and set requires gradient flag as True. 
x1 = torch.randn(10, 9)

