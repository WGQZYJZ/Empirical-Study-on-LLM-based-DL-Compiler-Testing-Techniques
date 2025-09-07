
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 512)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor # the other tensor is defined outside of Model, and the type must be float32 or float64
        v3 = torch.nn.functional.relu(v2) 
        return v3


# Initializing the model
m  = Model()
other_tensor = torch.randn(1024).to(dtype=torch.float32, device='cpu') # create a tensor with type float32 or float64 and shape (1024,)

# Inputs to the model
x1 = torch.randn(2, 1024)

 __output__  = m(x1)

