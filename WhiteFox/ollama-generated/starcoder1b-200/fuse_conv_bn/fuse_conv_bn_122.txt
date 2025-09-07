
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 10)

    def forward(self, x1):
        conv = torch.nn.functional.conv1d(...) # X can be 2 or 3 representing the dimension
        bn   = torch.nn.functional.batch_norm1d(...) # X should match with Conv1d
        return bn(conv(x1))


# Initializing the model
m = Model()


