
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v  = torch.cat([x1, x1], dim=0) + torch.cat([x1, x1], dim=0) + \
            torch.cat([x1, x1], dim=0)  # Concatenate the result tensor along axis 0
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
x2 = torch.randn(2, 3, 64, 64)
