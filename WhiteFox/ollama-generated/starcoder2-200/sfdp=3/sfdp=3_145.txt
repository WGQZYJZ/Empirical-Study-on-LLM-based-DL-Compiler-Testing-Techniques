
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.layer1 = torch.nn.Linear(4, 8)
        self.dropout = torch.nn.Dropout(0.5)
 
    def forward(self, x): 
        out_v1 = torch.matmul(x, torch.rand(32))
        out_v2 = self.layer1(out_v1) # Apply the dot product of the output tensor with a random tensor
        out_v3 = out_v2 * 0.5  # Multiply the output tensor by another constant
        out_v4 = torch.tanh(out_v3) # Apply tanh to the output of the convolution
        out_v5 = self.dropout(out_v4) # Apply dropout on the output of the convolution
        out_v6 = torch.matmul(x, out_v5)  # Compute the dot product between the output and the input
        return out_v2
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(32,4)
