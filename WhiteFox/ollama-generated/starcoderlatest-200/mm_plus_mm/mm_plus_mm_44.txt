
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input1 = torch.randn(256, 10)
        self.input2 = torch.randn(8, 3)
 
    def forward(self, x):
        v1 = torch.mm(x, self.input1)
        v2 = torch.mm(x, self.input2)
        return (v1 + v2).view(-1, v1.shape[0])


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(64, 3072)
