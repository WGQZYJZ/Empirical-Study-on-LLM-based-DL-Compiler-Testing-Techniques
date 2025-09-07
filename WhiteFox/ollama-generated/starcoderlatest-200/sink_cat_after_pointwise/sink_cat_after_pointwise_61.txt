
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU()
        self.tanh = torch.nn.Tanh()

    def forward(self, x1, x2):
        t1 = torch.cat([x1, x2], dim=0)
        t2 = t1.view(-1, 4)
        t3 = self.relu(t2)
        return self.tanh(t3)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 2, 100) # A random tensor with shape (batch_size x num_points x input_dim)
x2 = torch.randn(3, 2, 100) # A random tensor with shape (batch_size x num_points x input_dim)
