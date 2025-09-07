
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 3)
 
    def forward(self, x1):
        v0   = linear(x1) # Apply a linear transformation to the input tensor
 
        positive_mask  = (v0 > 0).float() * 1
        negative_mask  = -(v0 <= 0).float() * -0.2

        masked_out  = v0*negative_slope  # Implement the Leaky ReLU activation function
 
        v4   = torch.where(positive_mask, v0, negative_mask) # Choose between t1 and t3
        return v4
 
m  = Model()


# Initializing the model with valid tensors as input
x2  = torch.randn(64, 128)

__output__  = m(x2)

