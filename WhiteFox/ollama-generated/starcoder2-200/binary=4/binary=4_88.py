
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256*32+10, 2)
        self.softmax = torch.nn.Softmax()
 
    def forward(self, x1):
        v1 = torch.sigmoid(torch.tanh(x1))
        v2 = v1 + other_tensor 
        return v2


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(50)
 
 # Generating a new input tensor (to avoid potential in-place changes of the model inputs). This can be done by passing a new argument to the forward function:
__output__  = m(x1, other=other_tensor)

