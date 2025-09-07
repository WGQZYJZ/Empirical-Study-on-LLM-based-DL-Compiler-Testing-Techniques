
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.mm(x1, x2) + inp # Perform matrix multiplication on two input tensors and add the result to another tensor 'inp'


# Initializing the model
m = Model()


