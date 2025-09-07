
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2):
        v1 = torch.mm(input1, input2)
        t1 0.5
        return v6


# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
