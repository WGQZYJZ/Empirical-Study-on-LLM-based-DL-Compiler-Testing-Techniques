
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, input3, input4):
        v1 = torch.mm(x1, input2)  # Matrix multiplication between input1 and input2
        v2 = torch.mm(input3, input4)  # Matrix multiplication between input3 and input4
        return v1 + v2


# Initializing the model
m = Model()


