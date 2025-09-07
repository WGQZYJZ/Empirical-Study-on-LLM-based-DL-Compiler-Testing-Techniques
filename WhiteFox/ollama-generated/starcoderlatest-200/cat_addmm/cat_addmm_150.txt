
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 1024)
 
    def forward(self, x1):
        v1 = torch.addmm(x1, m_1, m_2) # Perform a matrix multiplication of mat1 and mat2 and add it to the input
        v2 = torch.cat([v1], dim)  # Concatenate the result along a specified dimension
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
