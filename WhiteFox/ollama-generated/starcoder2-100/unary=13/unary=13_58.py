
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(32 * 64 ** 2, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1)
        v3 = v2  * v1 # Apply the sigmoid function to the output of the linear transformation and then multiply the output of the sigmoid function by the output of the linear transformation. This is a typical pattern for a gating mechanism, where the sigmoid function controls the flow of information from the linear transformation
        return v3

# Initializing the model