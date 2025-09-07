
class Model(torch.nn.Module):
    def __init__(self, hidden_size=10):
        super().__init__()

        self.linear1 = torch.nn.Linear(2, hidden_size)
        self.linear2 = torch.nn.Linear(hidden_size, 3)

    def forward(self, x):
        v1 = x.permute(0, 2, 1)
        v2 = torch.nn.functional.conv2d(v1, self.linear1.weight, self.linear1.bias)

        # Use torch.max() to avoid a numerical error
        o2 = torch.max(v2, dim=-1)[0]

        # Use torch.mean() to get the average value of a given dimension in the input tensor
        v3 = torch.mean(o2, -1)

        return v3


# Initializing the model
m = Model()
__output__  = m(x1)


