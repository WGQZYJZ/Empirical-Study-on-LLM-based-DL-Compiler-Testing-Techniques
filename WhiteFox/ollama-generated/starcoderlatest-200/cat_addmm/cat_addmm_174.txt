
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(28*28, 300)
        self.fc2 = torch.nn.Linear(300, 500)
 
    def forward(self, x):
        v1 = torch.addmm(x, self.W_fc1, self.B_fc1) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2 = torch.relu(v1) # Apply an activation function on the output from the previous convolution layer
        v3 = torch.addmm(v2, self.W_fc2, self.B_fc2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        return v3
 
