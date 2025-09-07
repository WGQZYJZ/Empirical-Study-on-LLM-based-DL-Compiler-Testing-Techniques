
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc  = torch.nn.Linear(1024, 512)
 
    def forward(self, x):
        v1  = self.fc(x)
        v2  = torch.relu(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(30000, 512)
__output__  = m(x)

- If both `torch.nn.Linear` and `torch.nn.Conv2d` meet the criteria, the first example is selected as the final model that meets all the requirements.