
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.cat((x1, x2), dim=-1) # Concatenate two tensors with the last dimension equal to 1
        t1 = v1.permute(0, 2, 1)
        t2 = torch.nn.functional.linear(t1, ...) # or some other transformation function that does not depend on the size of v1
        ... # Other operations here
    return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 4)
x2 = torch.randn(32, 5)
