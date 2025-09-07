
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # Concatenate x1 and a scalar tensor with value of 2 to make a 3D tensor (b, c, d)
        t1 = torch.cat([x1, torch.tensor([[0]])], dim=1)

        # Reshape the concatenated x1 into (b, d * 2)
        t2 = t1.view(t1.shape[0], -1)

        # Apply a pointwise unary operation to get the output of ReLU on t2
        t3 = torch.relu(t2)

        # ...

# Initializing the model
m = Model()


