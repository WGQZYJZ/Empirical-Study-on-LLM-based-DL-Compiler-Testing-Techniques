
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v2  = torch.mm(x1[0], x1[1]) # Matrix multiplication between x1 and x1 at index 1 (input3)
        v4  = torch.mm(v2 , x1[2]) # Matrix multiplication between input2 multiplied by its transpose, and input4 (input3)
        v5  = v4 + v2 # Addition of the results of the two matrix multiplications
        return v5


# Initializing the model
m = Model()
