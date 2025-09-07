
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d(...)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.1, training=True) # Replace torch.nn.functional.dropout with lowmem_dropout
        v2 = self.dropout(v1)                              # Replace nn.Dropout2d with torch.nn.functional.dropout
        return torch.nn.functional.linear(v2, ...)


# Inputs to the model
x1 = torch.randn(1, 2, 2)
