
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):
        v1 = torch.permute(x1)  # Permute the input tensor A
        v2 = torch.bmm(v1, torch.permute(y1))

        return v2


# Initializing the model and inputs to it
m  = Model()

x1  = torch.randn(10, 5)
y1  = torch.randn(5, 8).permute(1, 0) # Permute the input tensor B in forward func

