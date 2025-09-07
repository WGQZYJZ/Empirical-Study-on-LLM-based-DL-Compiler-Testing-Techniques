
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, 3) # The weight is 3 by 2.
        v2 = v1.permute(-1,-2)                   # Permute the output tensor from the linear transformation with 2 by 3. 
        return v2

# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(4,50).float().cuda()

__output__  = m(x1)
