
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, query, key, value):
        v1 = self.conv(query) # Query convolution
        v2 = v1 * 0.5 # Multiply the output of the query convolution by 0.5
        v3 = v1 * 0.7071067811865476 # Multiply the output of the query convolution by 0.7071067811865476
        v4 = torch.erf(v3) # Apply the error function to the output of the query convolution
        v5 = v4 + 1 # Add 1 to the output of the query convolution
        v6 = v2 * v5 # Multiply the output of the query convolution by the output of the query convolution
        qk = torch.matmul(v6, key.transpose(-2, -1)) # Compute the dot product of the scaled dot product and the value tensor

        return v6
# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(1024, 3, 8, 8)
key = torch.randn(1024, 3, 8, 8)
value = torch.randn(1024, 3, 8, 8)
