
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.linear = torch.nn.Linear(8 * 32 * 32, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(64 * 64 * 3, -1)) # Reshape the input tensor from (BxCxD1xD2) to (B*C*D1*D2), then pass the result to linear layer with 8k*256 matrix
        v2 = torch.cat([v1], dim=1) # Concatenate the result along dim=1 and flatten it as a column vector
        return v2
 
 # Initializing the model
m = Model(dim=1)

 # Inputs to the model
x1 = torch.randn(64, 3, 64, 64)
