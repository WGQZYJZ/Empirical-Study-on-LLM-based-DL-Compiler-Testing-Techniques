
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Parameter(torch.randn((2, 8))) # Create a randomly generated query parameter with shape (2, 8)
        self.key  = torch.nn.Parameter(torch.randn((16, 8)), requires_grad=False) # Create the key parameter as the query parameter without requiring gradients
        self.value  = torch.nn.Parameter(torch.randn((240, 3)))
 
    def forward(self):
        vq  = torch.matmul(query, key.transpose(-2, -1)) # Compute the dot product of the query and the key
        vsk  = vq / (0.5 * 2)  # Scale the dot product by the inverse scale factor
        vs_qk = vsk.softmax(dim=-1)  # Apply softmax to the scaled dot product 
        output = vs_qk.matmul(value).div_(math.sqrt(8))

# Initializing the model
m  = Model()

