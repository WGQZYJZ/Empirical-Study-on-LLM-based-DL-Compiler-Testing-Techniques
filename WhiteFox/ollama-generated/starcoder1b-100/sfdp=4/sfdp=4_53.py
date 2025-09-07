
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = Attention()

    def forward(self, x1, x2):
        output  = self.attn(x1, x2)
        return output


# Initializing the model
m = Model()
