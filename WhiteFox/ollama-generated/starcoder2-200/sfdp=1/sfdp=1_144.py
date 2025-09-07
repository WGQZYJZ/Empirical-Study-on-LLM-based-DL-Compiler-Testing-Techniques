
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):  # Forward pass
        v1 = torch.matmul(x1, x2)  # Compute the dot product of two tensors
        v2 = torch.erf(v1)  # Apply the error function to the dot product
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(8, 3)  # Initialize a query tensor with shape (N, F_query)
x2 = torch.randn(3, 4)  # Initialize a key/value tensor with shape (F_key, F_value). The dot product will compute the inner matrix multiplication between these two tensors to obtain the output of the model

 __output__= m(x1)
 


