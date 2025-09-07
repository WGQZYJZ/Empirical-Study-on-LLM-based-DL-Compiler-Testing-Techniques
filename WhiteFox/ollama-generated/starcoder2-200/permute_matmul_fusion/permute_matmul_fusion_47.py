
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.permute(x1, 0, 2, 1) 
        v2  = torch.bmm(v1, torch.permute(x2, 0, 2, 1))
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
x1_shape  = (3,) + (1600) # This shape is specified by your algorithm
x2_shape  = (3,) + (5, 4800) # This shape is specified by your algorithm
x1  = torch.randn(*x1_shape)
x2  = torch.randn(*x2_shape)

