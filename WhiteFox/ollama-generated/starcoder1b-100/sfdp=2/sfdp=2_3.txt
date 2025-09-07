
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1d = torch.nn.Conv1d(3, 8, 1)
        self.fc = torch.nn.Linear(8, 8)
 
    def forward(self, x1):
        conv_output = self.conv1d(x1)
        output = self.fc(torch.relu(conv_output))
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(10, 3, 64, 64)
