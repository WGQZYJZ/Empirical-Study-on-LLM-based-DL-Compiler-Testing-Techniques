
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.matmul(v1, x2.transpose(-2, -1)) / math.sqrt(2.0 * math.pi) # Compute the dot product of the query and key tensors with square root
        v3 = torch.nn.functional.dropout(v2, p=dropout_p)
        return v3


# Initializing the model
m = Model()


