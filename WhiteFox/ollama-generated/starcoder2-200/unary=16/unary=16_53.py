
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.linear1 = torch.nn.Linear(3 * 64 * 64, 50)
        self.relu2 = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = self.relu2(v1)

        return v2

m = Model()

 # Inputs to the model 
x1 = torch.randn(10, 3 * 64 * 64) # Create an input tensor with size 10 x 57600 (in your model this size may vary depending on your specific architecture).

