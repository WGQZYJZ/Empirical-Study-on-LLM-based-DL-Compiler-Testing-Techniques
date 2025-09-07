
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 50)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + x1
        v3 = torch.nn.ReLU()(v2)
        return v3


# Inputs to the model
x1 = torch.randn(1, 64*64*3, requires_grad=True).view(-1, 128*50)
