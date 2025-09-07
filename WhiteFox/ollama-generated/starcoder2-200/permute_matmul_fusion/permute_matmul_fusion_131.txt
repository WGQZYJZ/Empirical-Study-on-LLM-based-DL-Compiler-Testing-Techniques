
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x0, x1):
        v0  = x0.permute(0, 2, 1).contiguous() # Permute the first input tensor, and convert its type to 'contiguous'
        v1  = torch.nn.functional.linear(v0, self.linear.weight, self.linear.bias)

        v3  = x1.permute(0, 2, 1).contiguous() # Permute the second input tensor, and convert its type to 'contiguous'
        v4  = torch.nn.functional.relu6(v3)
        
        return v1 + v4


# Initializing the model
m  = Model()

# Input tensors (tensors used as inputs in 'forward') with different shapes
x0 = torch.randn(2, 4, 5) # first input tensor A
x1 = torch.randn(3, 7, 8) # second input tensor B


# Inputs to the model
