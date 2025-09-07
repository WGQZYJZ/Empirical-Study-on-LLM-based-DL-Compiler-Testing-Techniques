
class Model(torch.nn.Module):
    def __init__(self, n=2):
        super().__init__()
        self.split = torch.nn.Conv1d(3, 8 * n, kernel_size=n)

    def forward(self, x0):
        splitted = []

        for i in range(x0.shape[0]):
            splitted.append(torch.split(x0[i], 16))

        x = torch.cat([x[-1] + t * -2 for t in splitted])
        return self.split(x)

# Initializing the model
n=2
m  = Model()


# Inputs to the model
x1 = torch.randn(3, n, 64)
