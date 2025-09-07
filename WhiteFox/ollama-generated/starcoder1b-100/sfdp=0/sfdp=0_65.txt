
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).view(1, -1)
        v2 = torch.sigmoid(torch.matmul(v1, self.key).transpose(-2, -1))  # Invert the dot product to obtain the query and key vectors
        v3 = torch.matmul(self.query, v2) / torch.sqrt(torch.abs(self.scale)) # Multiply the query vector by the inverse scaling factor for the key and value
        v4 = self.value * (v3 + 1)
        return torch.einsum('bhij,bjhk->bhki', (v4, self.softmax))

# Initializing the model
m = Model()


