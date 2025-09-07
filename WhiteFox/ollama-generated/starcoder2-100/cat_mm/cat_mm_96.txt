
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1  = torch.mm(x1, x2)
        v3 = [v1] * len(v1) # Creating the list from the result of matrix multiplication. The number depends on the input_tensor
        return torch.cat([i for i in v3], dim=0)

# Initializing the model
m  = Model()


# Inputs to the model
x1, x2  = [torch.randn(8, 64), torch.rand(5)] # Creating two input tensors, which are randomly generated.
__output__  = m(x1, x2)


