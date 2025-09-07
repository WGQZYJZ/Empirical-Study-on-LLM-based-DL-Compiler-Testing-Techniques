
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):

        # Input to the model should contain 3 tensors
        x2 = torch.randn(4096)
        x3 = torch.randperm(500).long()
        v1  = self.linear(x1, other=v2[None])
        v2  = self.linear(other=v1[:, 1], x2=v3[None].T)
        v3  = self.relu(x2=v1[None])

        return [v2, v3]

# Initializing the model and generating inputs for it
m = Model()

