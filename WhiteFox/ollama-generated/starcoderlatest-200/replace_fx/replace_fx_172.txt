
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0) # This node will not be replaced by `lowmem_dropout`
        v2 = self.dropout(v1, ...) # This node will trigger the lowmem_dropout optimization because of the '...' placeholder in the config file.
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3, 4)
