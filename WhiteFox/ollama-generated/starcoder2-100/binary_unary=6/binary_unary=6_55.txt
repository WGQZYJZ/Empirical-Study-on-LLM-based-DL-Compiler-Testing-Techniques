
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 10)

    def forward(self, x1): 
        v1 = self.linear(x1)        
        v2 = v1 - other_value   
        v3 = F.relu(v2)   
        return v3

# Initializing the model with different random values for 'other' and the initial values of the input tensor to be used in subsequent runs
m  = Model()
other_value  = torch.randn([1]).numpy()[0] # Set your preferred value for other here, which is then randomly initialized at every run.
initial_value  = np.array([[827], [634]])

