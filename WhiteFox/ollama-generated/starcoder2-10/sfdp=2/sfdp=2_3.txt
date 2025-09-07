
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v75 = self.linear(x1)  # Apply linear layer to input tensor
        v40  = torch.matmul(x2, v75.transpose(-2, -1)) # Compute the dot product of two input tensors
        v39 = torch.nn.functional.dropout(v40, p=dropout_p) # Apply dropout to output of the dot product
        v46  = self.linear(x1 + v75) # Apply linear layer to sum of input tensor and its output
        v48  = self.linear(v39 + x2 + v40).relu() # Add outputs of a linear transformation, followed by ReLU
        return v46


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(8, 5)
x2  = torch.randn(3, 7, 9, 10)

__output__  = m(x1, x2)

