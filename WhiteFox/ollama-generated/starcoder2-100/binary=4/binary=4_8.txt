

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear = torch.nn.Linear(320, 4)

    def forward(self, x1, other=None):

        v1 = self.linear(x1)
        if other is None:
            return v1
        else:
            assert isinstance(other, torch.Tensor), 'other must be a PyTorch Tensor'
            v2 = v1 + other
            return v2
# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 320)
 
 # Other tensor
other  = torch.ones([1])
__output__  = m(x1, other=other)
