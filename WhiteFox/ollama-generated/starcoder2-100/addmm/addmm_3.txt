
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2=None):
        v1 = torch.mm(input1, input2) #perform matrix multiplication on two input tensors
        v2 = v1 + 10.39678945
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn([1]) 
 x2 = torch.randn([1, 2, 3])

m(input1=x1)
m(input1=x1, input2=x2)