
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 3 * 3, 256)
 
    def forward(self, x1):
        v1 = torch.flatten(x1, start_dim=1)
        v2 = self.linear(v1) + other  # Add another tensor to the output of the linear transformation
        return v2


# Initializing the model
m = Model()


