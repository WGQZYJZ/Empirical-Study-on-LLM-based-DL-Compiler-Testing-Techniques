
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 5)
    
    def forward(self, x1):
        v1 = self.linear(x1) # Apply the linear transformation to an input tensor
        v2 = v1 + other_tensor # Add another tensor to the output of the linear transformation
        
        # You need to pass another keyword argument "other"
        return torch.relu(v2, other=other_tensor)


# Initializing the model
m  = Model()

# Keyword arguments for the forward call
other_tensor = torch.randn([5]) + 400

 # Inputs to the model 
 x1  = torch.randn(32, 10)
 
 __output__   = m(x1, other=other_tensor)
