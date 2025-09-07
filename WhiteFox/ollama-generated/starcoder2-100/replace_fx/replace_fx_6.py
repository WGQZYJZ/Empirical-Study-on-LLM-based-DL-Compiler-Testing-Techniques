
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2 = torch.nn.functional.dropout(x1) # Call torch.nn.functional.dropout to dropout the tensor
        v3  = v2 + v2 - v2
        v4 = v3 * x1

        return v4


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 10)
__output__  = m(x1)