
class Model(torch.nn.Module):
    def __init__(self, input1Size=(640,), input2Size=()):
        super().__init__()
        self.weight  = torch.nn.Parameter(data = torch.rand([3]))
        if len(input2Size) > 0:
            self.input2Size  = input2Size
        else : 
            self.input1Size  = [i*8 for i in input1Size]
 
    def forward(self, x):
        t0 = torch.mm(x[:, None], self.weight[None])
        t1  = t0 * math.pi / 6
        t2  = t1 + 0.5

        return (t2,)


# Initializing the model
m  = Model()


# Inputs to the model
x = torch.rand(4, len(m.input1Size))
x  = Variable(torch.from_numpy(x)).float()
x = Variable(torch.FloatTensor(x), requires_grad=True)
