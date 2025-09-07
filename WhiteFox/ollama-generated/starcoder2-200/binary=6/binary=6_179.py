
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(49, 13)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        return v1 - 2


m_new  = Model()

 # Inputs to the model