
class Model(torch.nn.Module):
    def __init__(self, input1 = torch.rand([32]), input2  = torch.rand([4])):
        super().__init__()
        self.conv  = torch.nn.Conv2d(input1 = 32)
        
    def forward(self):
        v0 = torch.mm(v01, v02)
        v1  = torch.cat((v0, v0))
        return v1

# Initializing the model
m = Model()

