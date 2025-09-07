
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28, 10)
 
    def forward(self, x1):
        v1 = torch.flatten(x1, start_dim=-1)  # Flatten the input tensor
        return self.linear(v1)


# Initializing the model
m = Model()


