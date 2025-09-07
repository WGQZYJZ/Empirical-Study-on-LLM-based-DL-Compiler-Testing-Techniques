
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(51200, 4)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.sigmoid(v1)
        v3  = v2 * v1
        return v3

# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(50, 4, 6400)
__output__  = m(x1)

# Answer-1: 
	model.py : 8.748
	inputs_to_model.pt: 8.739

