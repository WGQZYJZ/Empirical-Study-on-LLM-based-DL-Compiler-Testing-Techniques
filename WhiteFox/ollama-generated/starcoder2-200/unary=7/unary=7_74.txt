
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2048, 53)
 
    def forward(self, x1):
        v1  = self.linear1(x1)
        v2  = v1 * clamp(min=0, max=6, v1 + 3) / 6
        return v2


# Initializing the model and inputs to the model
m = Model()
x1 = torch.randn(48, 2048).type(torch.cuda.FloatTensor)

