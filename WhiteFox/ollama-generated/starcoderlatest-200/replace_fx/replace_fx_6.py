
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(p=0.5)

    def forward(self, x1):
        v2 = self.dropout(x1)
        return v2


# Initializing the model
m = Model()
m.dropout.training = True  # This line is added to mimic real-world usage where dropout layers are in eval mode when testing


# Inputs to the model
x1 = torch.randn(1, 2, 2)
