
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.nn.functional.linear(x1) 
        v2  = v.permute(-1, -3) # The permute method is invoked on the output tensor from the linear transformation.
        return v2


# Initializing the model
m = Model()


# Inputs to the model