
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout()

    def forward(self, x1):
        v1 = self.dropout(x1)  # Invoke the replace_fx method to generate replacement nodes and replace the original node's inputs with the replacement nodes' outputs
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
