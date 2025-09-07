
class ScaledDotProduct(torch.nn.Module):
    def __init__(self, model):
        super().__init__()
        self.model = model
 
    def forward(self, x1, x2):
        output  = self.model(x1)
        return (output @ x2.transpose(-2, -1)).softmax(dim=-1)


# Initializing the model
m = ScaledDotProduct(Model())


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
