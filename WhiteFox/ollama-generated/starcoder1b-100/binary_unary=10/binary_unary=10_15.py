
class Model(torch.nn.Module):
    def __init__(self, in_features: int = 256):
        super().__init__()
        self.linear1 = torch.nn.Linear(in_features=in_features, out_features=1)
 
    def forward(self, x):
        v1 = self.linear1(x)
        v2 = v1 + other
        return relu(v2)


# Inputs to the model
x  = torch.randn(100, 3, 144, 144)
