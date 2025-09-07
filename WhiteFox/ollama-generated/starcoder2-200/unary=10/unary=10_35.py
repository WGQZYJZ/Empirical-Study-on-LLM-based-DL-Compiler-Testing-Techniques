
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 10)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + 3
        v3 = torch.clamp_min(v2, 0) 
        v4 = torch.clamp_max(v3, 6) 
        v5 = v4 / 6 
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(8, 28*28).reshape(-1, 1, 28, 28) # 1 image of size (28 x 28), the batch_size should be at least one more than this number.
