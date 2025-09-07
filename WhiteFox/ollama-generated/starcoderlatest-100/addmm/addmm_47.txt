
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inp1: torch.Tensor, inp2: torch.Tensor):
        v1 = torch.mm(input1, input2) + inp # This line of code uses the 'inp' keyword argument that was passed as an argument in this method call to the forward function. 
        return v1


# Inputs to the model
x1 = torch.randn(50, 3, 64, 64)
x2 = torch.randn(50, 8, 64, 64)
