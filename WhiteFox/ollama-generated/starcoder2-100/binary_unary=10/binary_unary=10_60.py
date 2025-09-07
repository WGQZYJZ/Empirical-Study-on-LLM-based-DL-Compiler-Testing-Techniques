
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(640, 128)

    def forward(self, x1):
        v1 = self.linear(x1) 
        v3 = (v1 + other).relu() 
        return v3


# Initializing the model and feeding in input tensors
m  = Model()
x1  = torch.randn(500, 640) # Input tensor with shape [batch_size x 640] 
x2  = other  = torch.zeros(v3.shape).to(device)   # Input tensor of shape the same as v3


# Evaluating and getting outputs from the model on the inputs tensors
v1, v2 = m(x1), m(x2) 


