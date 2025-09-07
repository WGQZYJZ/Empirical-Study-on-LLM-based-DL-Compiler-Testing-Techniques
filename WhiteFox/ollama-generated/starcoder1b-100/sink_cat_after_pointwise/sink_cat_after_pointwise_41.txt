
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1, x2, ..., xn):
        v = torch.cat([x[i].view(-1) for i in range(len(x))], dim=0) # Reshape concatenated tensors (in dimension 0)
        return self.linear(v)


# Initializing the model
m = Model()


