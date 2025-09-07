
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1): 
        v3  = x1.permute(0, 2, 1) # Permute the input tensor
        v4  = torch.nn.functional.linear(v3, self.linear.weight, self.linear.bias) # Apply linear transformation to the permuted tensor.
        return v4

# Initializing the model
m_2 = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 2)
__output__  = m_2(x1)

