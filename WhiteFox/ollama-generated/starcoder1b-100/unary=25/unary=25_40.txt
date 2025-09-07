
class Model(torch.nn.Module):
    def __init__(self, input_size, hidden_size, out_size):
        super().__init__()
        self.conv  = torch.nn.Conv2d(input_size, hidden_size, kernel_size=1)
        self.linear = torch.nn.Linear(hidden_size, out_size)
 
    def forward(self, x):
        x = F.relu(self.conv(x))
        return self.linear(x)


# Initializing the model
m  = Model(3, 10, 4)


# Inputs to the model
x1 = torch.randn(1, 1, 64, 64)
