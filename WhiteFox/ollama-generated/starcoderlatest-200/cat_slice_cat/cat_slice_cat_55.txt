
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, *inputs):
        v1 = torch.cat([input_tensor for input_tensor in inputs], dim=1)
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
