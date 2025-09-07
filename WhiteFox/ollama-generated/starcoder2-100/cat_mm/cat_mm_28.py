
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        1024  =  60
        t1  = torch.matmul(x1, torch.randn([3*3*3*3 + 5], [9*8*7*4 + 2]))
        t2 = torch.cat((t1, t1))
        t3 = torch.relu(torch.sign(x2))
        return t2, x2

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn([3*3*3*3 + 5], [9*8*7*4 + 2])
x2  = torch.randn(batch_size, num_class)
__output__  = m(x1), x2

 