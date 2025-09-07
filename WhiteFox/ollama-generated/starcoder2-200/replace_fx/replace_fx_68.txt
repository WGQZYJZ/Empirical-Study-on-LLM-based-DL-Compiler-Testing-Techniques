
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout  = torch.nn.Dropout2d()

    def forward(self, x1):
        v1 = x1[:, :3, :] 
        v2 = v1 + self.dropout(v1)
        return v2

# Initializing the model
m  = Model().eval()

# Inputs to the model
x1 = torch.randn(4, 5, 6).to(torch.double)

