
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2, input3, input4):
        v1  = torch.mm(input1, input2) 
        v2  = torch.mm(input3, input4) # Addition of the results of two matrix multiplications
        return v1 + v2
 
m  = Model()

__inputs_1__ = (torch.randn(64, 8), torch.randn(8, 7))
__inputs_2__ = (torch.randn(350, 90), torch.randn(90, 150))
__inputs_3__ = m(__inputs_1__[0], __inputs_1__[1], __inputs_2__[0], __inputs_2__[1])

