
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1, x2, x3):
        v1 = x1.permute(0, 2, 1).view(-1, x1.shape[1]) # Reshape x1 into [-1, x1_dims] shape
        v2 = torch.cat([v1, x2], dim=1) # Concatenate v1 and x2 together along axis 1
        v3 = self.linear(v2)  # Apply linear transformation to tensor v2

        return v3


# Initializing the model
m = Model()


