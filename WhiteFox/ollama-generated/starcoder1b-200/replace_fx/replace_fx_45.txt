
class Model(torch.nn.Module):
    def __init__(self, dropout=0., replace_fx=True):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)
        self._dropout_rate = float(dropout)
        if replace_fx:
            self._drop = nn.Dropout(self._dropout_rate)

    def forward(self, x1):
        v1 = self._drop(x1)
        return torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)


# Initializing the model
m = Model()


