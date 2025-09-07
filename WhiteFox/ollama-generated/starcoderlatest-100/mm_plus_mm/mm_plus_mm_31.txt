
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(v1, v1)
        v3 = v1 + v2
        return v3


# Inputs to the model
x1 = torch.randn(10, 3, 4, 4) # Shape: [batch_size, channel_dim, h, w]
x2 = torch.randn(10, 5, 4, 4) # Shape: [batch_size, channel_dim, h, w]
