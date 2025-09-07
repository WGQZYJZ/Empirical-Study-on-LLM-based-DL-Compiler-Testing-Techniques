
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256 * 4, 8)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v0  = x1
        v1  = self.linear(v0)
        v3  = self.relu(v1) 
        return v3


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(4, 256 * 4) # This can be anything that conforms to shape (batch_size, input_features), where batch_size is usually small and 1 or greater
__output__  = m(x1).detach().numpy()


