
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(28*28, 10)
 
    def forward(self, x1):
        v1  = self.fc(x1)
        v2  = torch.relu(v1)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(30, 28*28)
__output__  = m(x1)

## A simple pytorch model example with public PyTorch APIs meets the specified requirements
- [ ] Generate a valid PyTorch model example with public PyTorch APIs meets the specified requirements

	## Model
	class Model(torch.nn.Module):
	    def __init__(self):
	        super().__init__()
	        self.conv = torch.nn.Conv2d(3, 8, 1)

	    def forward(self, x1):
	        v1  = self.conv(x1) 
	        return v1

	# Initializing the model
	m = Model() 

	## Inputs to the model
	x1  = torch.randn(256, 3, 28, 28) 
	__output__  = m(x1)

