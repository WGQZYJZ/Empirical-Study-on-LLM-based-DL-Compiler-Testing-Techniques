
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(30, 50)
 
    def forward(self, q1):
        v1 = self.qk(q1)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
q1  = torch.randn(128, 30) # Query tensor that needs attention calculation of size [batch_size x query_size]
__output__= m(q1)

