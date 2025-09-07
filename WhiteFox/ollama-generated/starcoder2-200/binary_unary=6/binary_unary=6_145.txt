
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 32, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - 0.5
        v3 = v2 > 0
        return v3


# Initializing the model and performing a forward pass to run the inference
m = Model()
output = m(torch.randn(1, 64 * 32))