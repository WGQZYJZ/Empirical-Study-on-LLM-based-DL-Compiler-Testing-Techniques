
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 10)

    def forward(self, x):
       v1  = torch.nn.functional.dropout(x, p=0.5) # Apply dropout to the input tensor
       v2  = torch.nn.functional.dropout(v1, p=0.3) # Apply dropout to the previous dropout result. 
       v3  = torch.rand_like(self.linear(v2), dtype=torch.float64, device='cpu') # Generate a tensor with the same size as input and dtype float64 filled with random numbers.
       return self.linear(v1) + self.linear(v3)

# Initializing model
m  = Model()


# Inputs to the model
x  = torch.randn(2, 500, 500, device='cpu') # Generate a random tensor with shape (batch_size=1, height=500, width=500) on CPU
__output__  = m(x).sum()

