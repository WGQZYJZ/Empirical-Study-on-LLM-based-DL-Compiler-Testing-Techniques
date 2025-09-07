
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*256, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1)) # Note the -1 here means that for each row in the input tensor, multiply all elements by `1` (that is, do not divide). The output size is `(batch_size*n_classes,)`
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64*256)
