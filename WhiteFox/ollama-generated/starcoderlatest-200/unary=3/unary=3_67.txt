
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.mean(x1)  # apply mean pooling to input tensor
        v2 = torch.abs(v1)
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
