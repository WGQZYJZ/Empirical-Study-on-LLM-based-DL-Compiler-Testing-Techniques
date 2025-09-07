
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.randn([32]) + 1
        v1 = self.linear0 = nn.Linear(784, 5)
        v2 = torch.tanh(v1(x)) + 2 
        v3 = torch.sigmoid(torch.cat([
            torch.relu6(-v2) * -0.9, 
            torch.leaky_relu(v2) / -v0, 
            self._activation_function_1(v2) * (-np.pi + np.e * 0.7)])).sum()
        return v3

# Initializing the model
m = Model()

