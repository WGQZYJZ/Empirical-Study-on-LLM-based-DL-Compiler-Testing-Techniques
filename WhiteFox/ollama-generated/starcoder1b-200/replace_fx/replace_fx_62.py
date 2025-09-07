
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.functional.dropout

    def forward(self, x1):
        t2 = self.dropout(x1, training=self.training)
        return t2


# Initializing the model
m  = Model()


__input__ = torch.randn(1, 2, 2)
