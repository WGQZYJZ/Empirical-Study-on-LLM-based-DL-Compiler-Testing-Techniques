
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1  = torch.nn.Linear(2, 3)
        self.linear2  = torch.nn.Linear(3, 4)

    def forward(self, x1):
        t1_permute = x1.permute([0, 2, 1]) 
        return self.linear1(t1_permute), \
            self.linear2(torch.bmm(x1, self.linear1.weight))

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(3, 4, 5)
x2  = torch.randn(3, 5)
__output__, __output___ = m(torch.rand(6))

