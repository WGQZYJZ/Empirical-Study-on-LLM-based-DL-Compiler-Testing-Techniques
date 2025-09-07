
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = Attention()

    def forward(self, x1, x2):
        return self.attn.forward(x1, x2)


# Initializing the model
m = Model()


