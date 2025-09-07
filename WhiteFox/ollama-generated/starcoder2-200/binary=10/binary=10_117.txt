
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) + other 
        return v1


# Initializing the model with additional tensor as input_tensor
m = Model()
other  = torch.randn(32) # An arbitrary tensor, not a PyTorch API call


