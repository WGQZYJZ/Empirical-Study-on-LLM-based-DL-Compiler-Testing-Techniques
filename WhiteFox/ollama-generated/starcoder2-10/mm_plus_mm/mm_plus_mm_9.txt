
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()
 
    def forward(self, x3, x4):
        v1 = torch.mm(x3, x4)
        return 0 * v1

