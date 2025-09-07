
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, inp):
        v = torch.mm(x1, inp) + inp  # Perform matrix multiplication on two input tensors and add the result to another tensor 'inp'
        return v


# Initializing the model
m = Model()


