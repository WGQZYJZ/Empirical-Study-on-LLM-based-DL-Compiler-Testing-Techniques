
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(64 * 64, 64)
 
    def forward(self, x1):
        v1 = x1.view(-1, 64 * 64) # Reshape the input tensor to [batch size, feature dimension]
        v2 = self.linear1(v1)
        return v2


# Initializing the model
m = Model()


## Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
