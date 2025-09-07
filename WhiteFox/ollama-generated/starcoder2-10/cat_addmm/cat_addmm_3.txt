
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v0 = torch.randn([3])  # Create an initial tensor of size (3)
        v1 = v0 + x1   # Add the input tensor to the first tensor
        v2 = v1 - x2   # Subtract the second input tensor from it
        v3 = v2 * v0   # Multiply the third input by the result of subtracting the second and third input tensors
        return v3

# Initializing the model with two input tensors, one output.
m  = Model()

__output__  = m(torch.randn([1]), torch.randn([2]))

