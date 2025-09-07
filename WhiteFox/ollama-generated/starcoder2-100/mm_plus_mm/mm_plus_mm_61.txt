
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1, input2, input3, input4):
        v1 = torch.mm(input1, input2)
        v2 = torch.mm(input3, input4)
        v3  = v1 + v2
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
input1 = torch.randn(50000, 784).to('cuda')
input2 = torch.randn(784, 999).to('cuda')
input3 = torch.randn(50000, 784).to('cuda')
input4 = torch.randn(784, 1000).to('cuda')
 
m(input1, input2, input3, input4)

