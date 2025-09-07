
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=0.5):
        v2 = torch.randn([3, 8], device="cpu") + 5
        v1 = self.conv(x1)
        v4 = v1 * other # Here we replace "other" with a tensor (in this case the input tensor)
        v6 = v2 + v4
 
        return v6


# Initializing the model: 
m = Model()

# Input to the model is a dummy tensor for "other". It will not be used during execution of the model. 
dummy_tensor  = torch.randn([1, 3, 64, 64])

# Inputs to the model with an additional argument: 
x1 = torch.randn(50, 8) # This is our input for the first tensor
other_input = torch.randn(10, 2) # We generate a random tensor for "other" here
 
