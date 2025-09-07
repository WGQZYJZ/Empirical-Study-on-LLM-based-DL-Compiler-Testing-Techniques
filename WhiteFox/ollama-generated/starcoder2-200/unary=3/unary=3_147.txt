
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1 * 0.7071067811865476
        v4  = torch.erf(v3) 
        v5  = v4 + 1
        v6  = v2 * v5

        return v6


# Initializing the model
m_initial  = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64) 
 
# Generating a new model and initial input
new_model  = Model()
initial_input = torch.randn(250, 80) # Any tensor of shape [N x d]
initial_output = m_initial(initial_input)
new_output  = new_model(initial_input)
 