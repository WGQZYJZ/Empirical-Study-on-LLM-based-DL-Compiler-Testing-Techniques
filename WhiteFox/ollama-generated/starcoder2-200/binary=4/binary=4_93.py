
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024*8*8, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = v1 + other_tensor
        return v2


# Initializing the model and setting the input tensor for "other"
m  = Model()
x1 = torch.randn(64*8*8, 1024) # shape of "other" should be 64*8*8 x 5

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

