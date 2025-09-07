
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input1 = torch.randn(3, 4)
 
    def forward(self, x2):
        v0 = torch.mm(x1, x2)
        return v0


# Initializing the model with one input tensor and two tensors as arguments
m = Model()
m(inp=torch.rand(2))

