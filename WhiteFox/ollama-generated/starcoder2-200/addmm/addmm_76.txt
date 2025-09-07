
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp=None):
        v1 = torch.mm(x1, x2)
        return v1 + v3


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(50, 4896),  # Tensor 1 of shape (N, M): N is number of samples in batch; M is the dimensionality of the input feature vector for a single sample.
x2 = torch.randn(3, 5)       # Tensor 2 of shape (M, K): M is the size of the input vector and K is the size of output vector
 

# Outputs from the model 
m(x1, x2, inp=0.)

