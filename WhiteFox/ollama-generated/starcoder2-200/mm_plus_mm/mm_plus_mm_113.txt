

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1=None, input2=None, input3=None, input4=None):  # inputs: torch.Size([16]), torch.Size([8]), torch.Size([9]), torch.Size([7])
        v1 = torch.mm(input1, input2)
        v2 = torch.mm(input3, input4)
        v3 = v1 + v2
        return v3

m  = Model()


__output__  = m(torch.randn(16),
    torch.randn(8),
    torch.randn(9),
    torch.randn(7))
