
class Model(torch.nn.Module):
    def __init__(self, dropout=0.5, fallback_random=True):
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)
        if fallback_random:
            self.rand_like = torch.randn_like

    def forward(self, x1):
        v1 = self.dropout(x1)
        return self.rand_like(v1)


# Initializing the model
m = Model()


