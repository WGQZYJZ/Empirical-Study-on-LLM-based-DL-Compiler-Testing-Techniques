
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        k = torch.randn(3, 4, 5) # Compute the dot product of a key and value tensor
        v = torch.randn(3, 4, 6) # Compute the dot product of a key and value tensor
        k = k * 2 # Scale the dot product by two (equivalent to multiplying by a constant 2).
        scale_factor = 1/k.norm(dim=0, keepdim=True)  # Compute the scale factor for dividing the dot products of key and value tensors.
        scaled_dot = torch.einsum("nch,ncd->ncb", k, v) / scale_factor # Scale the dot product by the scale factor.
        softmax_dot = scaled_dot.softmax(dim=-1)  # Apply softmax to the scaled dot product.
        output = torch.einsum("nc,nd->nhc", softmax_dot, x1) # Compute the dot product of the dropout output and the value tensor.
        return output


# Initializing the model
m = Model()

