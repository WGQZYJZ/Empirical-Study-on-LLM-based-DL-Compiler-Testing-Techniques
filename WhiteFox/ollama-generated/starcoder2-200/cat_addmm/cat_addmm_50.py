
class Model(torch.nn.Module):
    def __init__(self, num_hidden=128):
        super().__init__()
 
        self.hidden  = torch.nn.Linear(3 * 64 * 64 + num_hidden, num_hidden)
        self.out    = torch.nn.Linear(num_hidden, 50)
 
    def forward(self, input1, input2):
        t1  = torch.cat([input1, input2], dim=3)
        v1  = self.hidden(t1)
        return self.out(v1)


# Initializing the model
m = Model()
 
# Inputs to the model
i1  = torch.randn(8096, 45)
i2  = torch.randn(3 * 64 * 64 + 128, 8096)
__output__  = m(i1, i2)

