
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1024 * 5, 768)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor
        v3 = F.relu(v2) #F.relu is the ReLU activation function of torch
        return v3

# Initializing the model
m  = Model()
# Inputs to the model