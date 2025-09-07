
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, x2) # Performing matrix multiplication on two input tensors
        v2  = v1 + inp # Adding the result of the matrix multiplication to another tensor 'inp'
        return v2


# Initializing the model
m  = Model()
x1= torch.randn(4,5), x2 = torch.randn(5,6)

# Input tensors for the model
x3 = torch.randn(784).view([784, 1])
inp = torch.randn([784, 1])


__output__  = m(x1= x1, inp = input2)