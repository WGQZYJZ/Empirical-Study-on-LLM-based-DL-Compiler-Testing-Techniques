
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.inp = torch.zeros([10,])
 
    def forward(self, input1, inp=None):  # The 'inp' argument is passed as a keyword argument
        t1 = torch.mm(input1, torch.ones([50,2], dtype=torch.int))
        t2 = t1 + self.inp
        return t2


# Initializing the model
m = Model()

# Inputs to the model 
x1 = torch.randn([34,89])
