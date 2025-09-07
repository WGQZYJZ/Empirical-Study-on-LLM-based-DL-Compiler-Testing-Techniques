
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, 0) # No linear transformation to the input tensor
        v2 = v1.permute(0, 3, 1, 4).view(5, -1, 7) 
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(5, 28 * 28) # Input tensor with shape (batch_size=5, channel=28*28).