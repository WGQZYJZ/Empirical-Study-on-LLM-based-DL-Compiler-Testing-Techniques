
class Model(torch.nn.Module):
    def __init__(self, dropout_rate=0.1):
        super().__init__()
        self.dropout = torch.nn.Dropout(dropout_rate)

    def forward(self, x):
        return self.dropout(x)


# Inputs to the model
x = torch.randn(2, 3, 4)
__output = m(x)


