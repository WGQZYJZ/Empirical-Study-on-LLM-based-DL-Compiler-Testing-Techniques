
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = v1 + x1  # The addition of `v1` and itself is the result of applying the same pattern to the input x1
        return v2


# Initializing the model
m = Model()


