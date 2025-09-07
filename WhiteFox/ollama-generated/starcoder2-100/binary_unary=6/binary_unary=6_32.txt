
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3072,1536)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 - other
        return relu(v2)


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1536,1000) # Input tensor

# 'other' value (the number subtracted from the output of linear transformation)
other = float(randint(int(-2**(7 - 9)), int((8**9))))

