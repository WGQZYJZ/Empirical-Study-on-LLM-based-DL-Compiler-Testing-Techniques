
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(10, 5)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.tanh(v1)
        return v2


# Initializing the model and setting weights randomly in the tensors of all its parameters
m_init = Model()
for param  in m_init.parameters():
    param.data = torch.randn(*param.shape)


# Inputs to the model
x1  = torch.randn(3, 10)
__output__  = m_init(x1)
