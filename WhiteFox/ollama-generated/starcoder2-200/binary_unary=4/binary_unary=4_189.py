
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256, 4096)
 
    def forward(self, x1, other=None):
        v1  = self.linear(x1)
        if other is not None:
            v2  = v1 + other
        else:
            raise Exception("other is empty")
        
        v3  = torch.relu(v2) 
        return v3


# Initializing the model
m  = Model()
 
# Input tensors to the model, which contains the argument `other`
x1  = torch.randn(6400, 512, requires_grad=True) # 6400 is the batch size in this example
other  = torch.randn(6400, 512, requires_grad=True)
 
# Forward pass using the model and input tensors with the argument `other`
__output__  = m(x1, other)

