
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.functional.dropout(x1, p=0.4) # Apply dropout to the input tensor with probability 0.4
        return v1


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(2, 3, 5)
__output__  = m(x1)