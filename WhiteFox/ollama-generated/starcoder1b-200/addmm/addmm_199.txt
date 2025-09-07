
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, inp1, inp2):
        return inp1 + inp2

# Initializing the model
m = Model()

