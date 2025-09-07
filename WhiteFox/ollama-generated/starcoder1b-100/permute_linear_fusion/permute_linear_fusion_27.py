
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = self.linear(v1)
        return v2


# Initializing the model
m1 = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)
__output1 = m1(x1)


# Inputs to the model
x2 = torch.randn(1, 2, 4)
__output2 = m1(x2)

# The expected output of this test is as follows:
# __output == __output1

assert isinstance(__output1, tuple)
assert isinstance(__output2, tuple)


## Additional requirements:
