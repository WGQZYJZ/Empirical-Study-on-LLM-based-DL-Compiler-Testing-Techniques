
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(3072, 1)
 
    def forward(self, x1):
        v1  = self.fc(x1)
        return torch.relu(v1)


# Initializing the model
m  = Model()
 
# Inputs to the model
__input_tensor__  = torch.randn(3072).reshape(-1, 64 * 85 * 96)
 
  # Compute the output of the model
__output__  = m(__input_tensor__)
