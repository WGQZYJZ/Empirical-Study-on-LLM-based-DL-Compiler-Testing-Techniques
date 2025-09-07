
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1000 * 3, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        return relu(v1)

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3072) # Input tensor with size [batch_size=1 x 3072] = 1*3072 = 3072
