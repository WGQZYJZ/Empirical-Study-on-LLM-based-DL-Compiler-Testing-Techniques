
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1) # Permute the input tensor A with (batch_size, H1, W1, C1)
        v2 = x2.permute(0, 2, 1) # Permute the input tensor B with (batch_size, H2, W2, C2)
        out = torch.bmm(v1, v2) # or torch.matmul(v1, v2)
        return out


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 4, 3)
x2 = torch.randn(1, 2, 5, 6)
