
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.bmm(x1.permute(0, 2, 1), x2) # The permuted tensor is passed as one of the arguments to a function call
        return v1


# Initializing the model