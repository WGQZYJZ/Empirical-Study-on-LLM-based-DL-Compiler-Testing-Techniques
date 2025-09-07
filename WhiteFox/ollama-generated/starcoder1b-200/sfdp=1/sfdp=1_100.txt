
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        vq = torch.matmul(x1, x2)  # Compute the dot product of the query and key tensors
        vq = vq.div(torch.pow(vq, inv_scale_factor))  # Scale the dot product by the inverse scale factor
        vq = vq.softmax(dim=-1)  # Apply softmax to the scaled dot product
        v2 = vq.matmul(value)  # Compute the dot product of the dropout output and the value tensor
        return v2


# Initializing the model
m = Model()


