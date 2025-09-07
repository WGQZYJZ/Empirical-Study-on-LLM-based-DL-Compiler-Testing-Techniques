
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = torch.permute(x1, [0, 2, 1]) # Permute the input tensor A
        v3  = torch.bmm(v1, self.weight)   # or torch.matmul(v1, self.weight)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model (inferred)
