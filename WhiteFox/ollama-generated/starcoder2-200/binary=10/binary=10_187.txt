
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*3, 10)
 
    def forward(self, x2):
        v1 = self.linear(x2)
        return v1


# Initializing the model
m = Model()

 # Inputs to the model
x2 = torch.randn(1, 3 * 64)

# Add a constant 5 to each element of the output of the linear transformation
other = torch.tensor([[5 for i in range(v1.shape[0])] for j in range(v1.shape[1])]).transpose((1, 0)).to('cuda' if torch.cuda.is_available() else 'cpu')

 # Outputs from the model on different inputs
