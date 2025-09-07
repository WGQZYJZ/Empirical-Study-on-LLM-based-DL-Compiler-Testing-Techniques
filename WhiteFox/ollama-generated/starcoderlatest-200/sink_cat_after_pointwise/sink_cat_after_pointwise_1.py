
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0) # concatenate along the batch dimension
        t2 = t1.view(-1, 4) # reshape to a tensor with shape [batch_size, feature_dim]
        return self.relu(t2)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 3)
x2 = torch.randn(4, 3)
