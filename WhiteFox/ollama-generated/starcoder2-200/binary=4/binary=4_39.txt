
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1) + torch.randn(x1.shape).cuda() # Add a random tensor to the output of the linear transformation (assuming the input is on GPU)
        return v1


# Initializing the model 
m = Model()

# Input tensors
x1 = torch.randn(4, 512).to("cuda")

