
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.randn([3])
        v3  = self.linear(x1) 
        v4  = v3 + v2
        return v4

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(78, 1024)

 # Generate a new model with the same forward function as the previous one (m). 

new_m = copy.deepcopy(m)
# Inputs for the new model
new_input = x1
