
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        v3 = torch.nn.functional.conv2d(v1, v5)  # convolution and batch normalization
        return v4, v6


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(batch_size, 3, 9, 9)
x2  = torch.randn(batch_size, 5, 7, 7)
x3  = torch.randn(batch_size, 640, 14, 14)


__outputs__ = m((x1, x2))