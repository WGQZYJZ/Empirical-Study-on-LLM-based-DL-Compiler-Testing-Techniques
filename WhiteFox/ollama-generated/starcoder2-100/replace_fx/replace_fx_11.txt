
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t3 = torch.nn.functional.dropout(x1, p=0.5) # Permute the input tensor by specifying a probability of 0.5 for dropout
        return t3

# Initializing the model
m = Model()

# Inputs to the model
__input__ = torch.rand((2, 4))

