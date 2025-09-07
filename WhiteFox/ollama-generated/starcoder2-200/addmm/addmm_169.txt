
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.functional.linear
 
    def forward(self, x1): 
        v2  = mm(x1) # Perform matrix multiplication on two input tensors
        return inp * v2 + v3


# Initializing the model
m = Model()

# Inputs to the model
inp = torch.randn([64])
x1 = torch.randn([5, 900])
