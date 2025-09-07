
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.nn.functional.linear(x1, 0, None) # Get the output tensor from linear
        return t1


# Initializing the model
m = Model()


