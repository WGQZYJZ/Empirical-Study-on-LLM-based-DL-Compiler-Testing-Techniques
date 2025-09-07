
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(3, 4)
 
    def forward(self, x1):
        t1 = torch.mm(x1, x1) # Matrix multiplication of two input tensors
        t2 = t1[:, :, 0]  # Extract the first row of the matrix `t1` using `[]` operator and assign it to `t2`
        t3 = nn.functional.relu(self.fc1(t2))  # ReLU activation function
        return t3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
