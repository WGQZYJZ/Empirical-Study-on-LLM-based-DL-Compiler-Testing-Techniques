
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2401, 5)
 
    def forward(self, x):
        t1 = self.linear(x)
        t2 = torch.sigmoid(t1)
        t3 = t1 * t2
        return t3


# Initializing the model
m = Model()
 
# Inputs to the model
input_tensor  = torch.randn([8,5])
 
 # Generating the output of the model using input tensor and previous model
 