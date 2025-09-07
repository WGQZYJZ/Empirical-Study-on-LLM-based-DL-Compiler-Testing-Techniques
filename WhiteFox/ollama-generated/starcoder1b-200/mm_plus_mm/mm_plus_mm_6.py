
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, input5):  # Please also specify the input of `input5` here (it may be a Tensor).
        v1 = torch.mm(x1, x2) + input5
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
input2 = torch.randn(8, 7, 64, 64)
input3 = torch.randn(1, 7, 64, 64)
input5 = torch.randn(4, 3, 64, 64)
