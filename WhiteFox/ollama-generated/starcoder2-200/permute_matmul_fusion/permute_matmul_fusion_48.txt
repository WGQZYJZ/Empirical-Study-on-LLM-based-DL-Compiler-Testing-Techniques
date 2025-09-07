
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 1)

    def forward(self, x1, y):
        v0  = x1 + y # Add two tensors with the same shape and broadcast.
        v1  = v0[None,:,:] # Create a new dimension along the channel direction of the input tensor by squeezing.
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias) 
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(500, 3, 2, 4, 6).transpose(2, 4) 
 # Generate the broadcast tensor that is a result of broadcasting two tensors with shape: [None, None, 2] and [None, 4, None]. 
 y = torch.randn(500, 3)

