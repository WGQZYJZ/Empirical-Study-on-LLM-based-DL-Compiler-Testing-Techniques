
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.randn((32, 64))
        self.key = torch.randn((512, 80))
 
    def forward(self, value):
        v1  = query  @ key.transpose(-2, -1) # Compute the dot product of a randomly generated query and key tensors
        v2  = v1 / 4e-6  # Scale the dot product by an inverse scale factor
        v3  = torch.nn.functional.softmax(v2, dim=-1)  # Apply softmax to the scaled dot product
        v4  = dropout_qk(v3) @ value  # Compute the dot product of the dropout output and a randomly generated value tensor
        return v4

# Initializing model