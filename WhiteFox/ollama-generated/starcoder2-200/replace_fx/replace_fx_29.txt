
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout(0.2)

    def forward(self, x1):
        v1  = self.dropout(x1)
        v2  = torch.rand_like(v1, memory_format=torch.channels_last) 
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 4)
