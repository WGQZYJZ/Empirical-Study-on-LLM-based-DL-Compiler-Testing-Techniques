
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(3, 1)
 
    def forward(self, x):
        return torch.relu(self.fc(x))

 # Initializing the model
m = Model()

 # Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
output_tensor = m(input_tensor)