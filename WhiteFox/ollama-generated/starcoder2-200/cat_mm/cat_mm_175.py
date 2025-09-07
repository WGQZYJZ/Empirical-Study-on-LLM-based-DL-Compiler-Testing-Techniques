
class Model(torch.nn.Module):
    def __init__(self, list1):
        super().__init__()
 
    def forward(self, input1, input2):
        v1  = torch.mm(input1, input2) # Matrix multiplication of two input tensors
        v2 = torch.cat([v1 for i in range(len(list1))])
        return v2


# Initializing the model
m = Model([4096]*3)
__output__  = m(torch.randn(1, 512), torch.randn(784, 512))

