
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(24 * 3, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return v1


# Initializing the model
m = Model()
 
# Input tensors to the model
x1 = torch.randn(7, 24 * 3).cuda() # Note that input tensors should be on CUDA devices for the model to function correctly
x2 = torch.tensor([5]).cuda() # Note that the tensor 'other' is on CUDA device as well
 
# Initializing dummy outputs
__output_before__, __output_after__  = m(x1), m(x2)

