
class Model(torch.nn.Module):
    def __init__(self, num=1024*7 * 3):
        super().__init__()

    def forward(self, input1, input2, input3, input4):
        v1 = torch.mm(input1, input2)
        v2 = torch.mm(input3, input4)
        v3 = v1 + v2
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
inp1  = torch.randn(7 * 1024, 512).type(torch.FloatTensor)
inp2  = torch.randn(512, 64).type(torch.FloatTensor)
inp3  = torch.randn(7*1024, 64).type(torch.FloatTensor)
inp4  = torch.randn(64, 1024).type(torch.FloatTensor)

 # Initializing the target tensor to store the output of the model
out = torch.zeros([3])
__output__  = m(inp1, inp2, inp3, inp4)

