
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        v1  = torch.mm(input1, input2) 
        v2  = torch.mm(v1, 50.0).cuda()
        return v2

# Initializing the model
m  = Model().eval()

 # Inputs to the model
input1  = torch.rand([8], dtype=torch.float32).cuda()
input2  = torch.rand([7], dtype=torch.float32).cuda()

__output__  = m(input1, input2)

