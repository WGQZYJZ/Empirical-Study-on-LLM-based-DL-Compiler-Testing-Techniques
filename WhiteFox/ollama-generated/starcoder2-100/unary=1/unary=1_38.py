
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8)
 
    def forward(self, x2):
        v7 = self.linear(x2)
        v8 = v7 * 0.5
        v9 = (v7*v7*v7)*0.044715
        v10 = v9 + v8 
        v11 = v10 * 0.7978845608028654
        v12 = torch.tanh(v11)
        v13 = v12 + 1  
        return v7*v13


# Initializing the model and generating inputs to it.
n = Model()
x2  = torch.randn(1, 1)*10 # The input is a one dimensional tensor.
