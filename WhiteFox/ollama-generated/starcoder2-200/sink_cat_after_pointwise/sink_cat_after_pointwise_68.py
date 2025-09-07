
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=3)
        v2 = v1.view(-1, 4 * 6 + 6)
        v3 = torch.nn.functional.linear(v2, 50, 9)
        return v3


# Initializing the model
m = Model()
x1_shape  = [8] # Shape of the first input tensor: (8,)
x2_shape  = [4] # Shape of the second input tensor: (4,)

# Inputs to the model
__input_tensors__  = {'x1': torch.randn(*x1_shape), 'x2': torch.randn(*x2_shape)}


