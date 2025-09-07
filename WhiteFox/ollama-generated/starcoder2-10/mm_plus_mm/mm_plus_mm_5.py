
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, x3, x4):  # input1, input2, input3 and input4 are already declared variables with their dimensions as defined in the next line.
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v3


m  = Model()
input1 = torch.randn(5,60) # This is the variable that should be randomly generated with 5 rows and 60 columns according to PyTorch rules.
input2 = torch.randn(5,48) # These two variables will have the same dimensions of the previous two.
input3 = torch.randn(70,100) # The dimensions of these two variables are already defined.
input4  = torch.randn(69,100) # The dimensions of these two variables are already defined.


__output__  = m(input1, input2, input3, input4)
