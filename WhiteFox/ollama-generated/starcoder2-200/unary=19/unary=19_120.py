
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32 * 32 * 3, 10)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
input_data = np.random.randn(32 * 32 * 3).astype('float') # Input data should have the same shape as that of the first parameter in self.linear
x1 = torch.from_numpy(input_data)
