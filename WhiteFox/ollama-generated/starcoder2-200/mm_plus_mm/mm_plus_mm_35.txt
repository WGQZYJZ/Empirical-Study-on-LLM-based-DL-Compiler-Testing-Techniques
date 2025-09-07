
class Model(torch.nn.Module):
    def __init__(self, n1, n2, n3):
        super().__init__()
        self.linear1  = torch.nn.Linear(n1 + n2, n1)
        self.linear2  = torch.nn.Linear(n1 * n2, n1)
 
    def forward(self, x1, x2, x3):
        v1  = self.linear1(torch.cat((x1, x2), dim=1)) # Apply the linear transformation with weight shape (N1 + N2, N1). 
        v2  = torch.mm(v1, v1.T) # Apply the matrix multiplication of the output of the linear transformation between input tensors
        v3  = self.linear2(torch.cat((x3[:, :, None], x3[:, None]), dim=1))  # Apply a linear transformation with weight shape (N1 * N2, N1), where N1 is equal to the size of the third dimension in the input tensor.
        v4  = torch.mm(v1, v3)  # Multiply output of the first matrix multiplication between input tensors by another matrix multiplication results 
        return v4

# Initializing the model
m  = Model(20, 15, 78)

