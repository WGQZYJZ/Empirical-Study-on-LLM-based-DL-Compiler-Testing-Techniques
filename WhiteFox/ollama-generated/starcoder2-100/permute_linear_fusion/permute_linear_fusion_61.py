
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):

        v1  = x1.permute(0, 2, 1)
        v3  = 5
        v4  = torch.add(v1, 7) # An additional tensor is added to the permuted one
        v2  = torch.nn.functional.linear(v4, self.linear.weight, self.linear.bias)

        return v2


# Initializing the model